import time
import numpy as np
import MathAndOperations

# Global obstacle list
ObstacleList = []


class Map:
    def __init__(self, mapsize=(1920, 1080)):
        """
        mapsize: (width, height) şeklinde verilen harita boyutu.
        Ekrana sığdırmak için uygun bir çarpan bulunuyor.
        """
        screenx, screeny, multiply = self.findMapSize(mapsize)
        self.screensize = (screenx, screeny)
        self.pixelsize = round(1 / multiply, 3)

    def findMapSize(self, mapsize):
        screenx, screeny = mapsize[0], mapsize[1]
        multiply = 2

        # Harita ekran boyutundan küçükse büyüterek sığdır
        if mapsize[0] < 1920 and mapsize[1] < 1080:
            while True:
                screenx = mapsize[0] * multiply
                screeny = mapsize[1] * multiply
                if screenx > 1920 or screeny > 1080:
                    multiply -= 1
                    break
                multiply += 1
            return mapsize[0] * multiply, mapsize[1] * multiply, multiply

        # Harita ekran boyutundan büyükse küçülterek sığdır
        else:
            while True:
                screenx = mapsize[0] / multiply
                screeny = mapsize[1] / multiply
                if screenx < 1920 or screeny < 1080:
                    multiply -= 1
                    break
                multiply += 1
            return int(mapsize[0] / multiply), int(mapsize[1] / multiply), 1 / multiply


class Obstacles:
    def __init__(self, Coords, Roughness="Infinity"):
        global ObstacleList

        self.Coords = Coords
        self.InsideCoords = []
        self.Edges = []
        self.Roughness = Roughness
        self.MeanPoint = []

        # Global listeye ekle
        ObstacleList.append(self)

        self.CoordsToEdges()
        self.Detect_MeanPoint()

        # Roughness sonsuz değilse iç koordinatlar oluştur
        if self.Roughness != "Infinity":
            self.InsideCoords = self.ShiftCoords(number=-1)
            self.InsideCoords.append((self.MeanPoint[0], self.MeanPoint[1]))

        # Çakışmayı önlemek için Coords'i kaydır
        self.Coords = self.ShiftCoords()

    def CoordsToEdges(self):
        index = 0
        while index != len(self.Coords) - 1:
            self.Edges.append((self.Coords[index], self.Coords[index + 1]))
            index += 1
        self.Edges.append((self.Coords[index], self.Coords[0]))

    def Detect_MeanPoint(self, axis=0):
        self.MeanPoint = np.mean(self.Coords, axis=axis)

    def ShiftCoords(self, number=1):
        new_coords = []

        # Koordinatları biraz kaydırarak kendi kenarlarıyla çakışmasını engelle
        for coord in self.Coords:
            if coord[0] > self.MeanPoint[0]:
                new_coords_x = coord[0] + number
            else:
                new_coords_x = coord[0] - number

            if coord[1] > self.MeanPoint[1]:
                new_coords_y = coord[1] + number
            else:
                new_coords_y = coord[1] - number

            new_coords.append((new_coords_x, new_coords_y))

        return new_coords
        # Not: Eğer x,y meanpoint'ten büyükse sağa/aşağı kaydırılmış olur.


class Ways:
    def __init__(self, ObstaclesList=None):
        if ObstaclesList is None:
            ObstaclesList = []

        self.ObstaclesList = ObstaclesList
        self.Pair_List = []
        self.Path_List = []

        self.Create_Rough_Ways()
        self.Create_PairList()
        self.Create_Ways(self.Pair_List)

    def Create_Ways(self, GivenPairs=None, Roughness=False):
        if GivenPairs is None:
            GivenPairs = []

        for pairs in GivenPairs:
            can_draw = True
            for obstacle in self.ObstaclesList:
                for edge in obstacle.Edges:
                    if MathAndOperations.MathOperations.doesCollide(self, pairs, edge):
                        can_draw = False
                        break
                if not can_draw:
                    break

            if can_draw:
                if Roughness is not False:
                    length = MathAndOperations.MathOperations.LenghtOfPaths(
                        self, pairs, roughness=Roughness
                    )
                    self.Path_List.append((pairs[0], pairs[1], length))
                else:
                    length = MathAndOperations.MathOperations.LenghtOfPaths(
                        self, pairs
                    )
                    self.Path_List.append((pairs[0], pairs[1], length))

    def Create_Rough_Ways(self):
        """
        doesCollide fonksiyonu için sadece rough koordinatlardan oluşan
        kaba bir pair listesi üretir.
        """
        for obstacle in self.ObstaclesList:
            Rough_Pairlist = []
            if obstacle.Roughness != "Infinity":
                # Bir engelin insideCoord'ları ile diğer engellerin coords'lerini eşle
                for pair in obstacle.InsideCoords:
                    for objects in self.ObstaclesList:
                        if objects.Roughness != "Infinity":
                            for coords in objects.Coords:
                                Rough_Pairlist.append((pair, coords))

                # Engelin kendi insideCoord'ları arasındaki kombinasyonlar
                for inside in MathAndOperations.itertools.combinations(
                    obstacle.InsideCoords, 2
                ):
                    Rough_Pairlist.append(inside)

                # Dış coords ile insideCoords'leri bağla
                for value, coord in enumerate(obstacle.Coords):
                    length = MathAndOperations.MathOperations.LenghtOfPaths(
                        self,
                        [coord, obstacle.InsideCoords[value]],
                        roughness=obstacle.Roughness,
                    )
                    self.Path_List.append(
                        (coord, obstacle.InsideCoords[value], length)
                    )

                # Rough pair list üzerinden mümkün yolları oluştur
                self.Create_Ways(Rough_Pairlist, obstacle.Roughness)

    def Create_PairList(self):
        """
        Tüm koordinatları tek listede toplayıp aralarındaki tüm kombinasyonları üret.
        """
        PairList = []
        for obstacle in self.ObstaclesList:
            for coords in obstacle.Coords:
                PairList.append(coords)

        # Tüm koordinatlar arasındaki kombinasyonlar
        for pair in MathAndOperations.itertools.combinations(PairList, 2):
            self.Pair_List.append(pair)


class Points:
    def __init__(self, coords, Way):
        self.Coord = coords
        self.Roughness = "Infinity"

        check = self.IsItInside(Way.ObstaclesList)
        PairList = self.AddPointsToPairList(Way.ObstaclesList)

        if check:
            Way.Create_Ways(PairList, self.Roughness)
        else:
            Way.Create_Ways(PairList)

    def IsItInside(self, GivenObstacleList=None):
        """
        Noktanın herhangi bir engelin içinde olup olmadığını kontrol eder.
        İçindeyse Roughness engelin Roughness'i olur.
        """
        if GivenObstacleList is None:
            GivenObstacleList = []

        for obstacle in GivenObstacleList:
            if obstacle.Roughness != "Infinity":
                counter = 0
                for edge in obstacle.Edges:
                    # Engelin kenarlarının fonksiyonlarını oluştur
                    slope, constant = MathAndOperations.MathOperations.FunctionsOfEdges(
                        self, edge
                    )
                    y = (slope * obstacle.MeanPoint[0]) + constant
                    y2 = (slope * self.Coord[0]) + constant

                    if slope != 0:
                        try:
                            x = (obstacle.MeanPoint[1] - constant) / slope
                            x2 = (self.Coord[1] - constant) / slope
                        except ZeroDivisionError:
                            x, x2 = y, y2
                    else:
                        # slope == 0 ise x değerlerini y ile temsil ediyoruz
                        x, x2 = y, y2

                    # Nokta meanpoint ile aynı tarafta mı kontrolü
                    if y <= obstacle.MeanPoint[1] and y2 < self.Coord[1]:
                        counter += 1
                    elif y > obstacle.MeanPoint[1] and y2 > self.Coord[1]:
                        counter += 1
                    elif x < obstacle.MeanPoint[0] and x2 < self.Coord[0]:
                        counter += 1
                    elif x > obstacle.MeanPoint[0] and x2 > self.Coord[0]:
                        counter += 1

                # Eğer tüm kenarlar için aynı taraftaysa nokta engelin içindedir
                if counter == len(obstacle.Edges):
                    self.Roughness = obstacle.Roughness
                    return True

        return False

    def AddPointsToPairList(self, GivenObstacleList=None):
        if GivenObstacleList is None:
            GivenObstacleList = []

        PairList = []
        for obstacle in GivenObstacleList:
            for coord in obstacle.Coords:
                PairList.append((self.Coord, coord))
            for coord in obstacle.InsideCoords:
                PairList.append((self.Coord, coord))

        return PairList

    def AppendPointsToMap(self, Way):
        """
        Noktayı sonradan eklemek için kullanılabilir.
        """
        check = self.IsItInside(Way.ObstaclesList)
        PairList = self.AddPointsToPairList(Way.ObstaclesList)
        if check:
            Way.Create_Ways(PairList, self.Roughness)
        else:
            Way.Create_Ways(PairList)


def main():
    global ObstacleList

    start_time = time.time()

    # *************    IDENTIFIED   OBJECTS    *************

    # Dikkat: içbükey (concave) şekilleri doğrudan tanımlama.
    # Bölüp dışbükey (convex) parçalara ayırmak gerekiyor.

    Infinity1 = Obstacles(
        [(270, 202), (287, 258), (356, 316), (307, 399), (229, 416), (172, 349)]
    )

    Infinity2 = Obstacles(
        [(138, 626), (256, 748), (346, 752), (480, 906), (307, 1004), (73, 947), (49, 796)]
    )

    Infinity3 = Obstacles(
        [(402, 708), (358, 570), (463, 404), (640, 209),
         (795, 191), (833, 241), (857, 385), (783, 461)]
    )

    Infinity4 = Obstacles(
        [(664, 652), (747, 712), (864, 659), (1084, 703),
         (1118, 823), (1080, 975), (724, 962), (488, 813)]
    )

    Infinity5 = Obstacles(
        [(984, 118), (1093, 95), (1115, 238), (1023, 287), (947, 252)]
    )

    Infinity6 = Obstacles(
        [(1025, 391), (1191, 337), (1296, 361), (1353, 493),
         (1153, 663), (1025, 579)]
    )

    Rough1 = Obstacles([(897, 423), (926, 495), (986, 461), (975, 418)], Roughness=3)

    Rough2 = Obstacles([(147, 455), (219, 457), (203, 551), (166, 545)], Roughness=4)

    Rough3 = Obstacles(
        [(706, 525), (797, 630), (1017, 617), (997, 397), (908, 365)],
        Roughness=1.8,
    )

    Rough4 = Obstacles(
        [(85, 503), (124, 424), (278, 451), (250, 596), (132, 578)],
        Roughness=2,
    )

    # *************    IDENTIFIED   OBJECTS    *************

    Way = Ways(ObstacleList)

    # Buradaki asıl düzeltme: dtype=object ile kaydetme
    np.savez(
        "Map_01",
        ObstacleList=np.array(ObstacleList, dtype=object),
        Paths=np.array(Way.Path_List, dtype=object),
    )
    # Yüklerken:
    # data = np.load("Map_01.npz", allow_pickle=True)
    # ObstacleList_loaded = data["ObstacleList"]
    # Paths_loaded = data["Paths"]

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
