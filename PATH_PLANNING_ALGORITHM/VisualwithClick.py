import cv2
from Map import Obstacles
import numpy as np 
import MathAndOperations
import Map
import time
import PlanningAlgorithms
import copy


image=cv2.imread("map_01.png")




np_load_old = np.load
# modify the default parameters of np.loadWe
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
MapNp=np.load("Map_01.npz")
# call load_data with allow_pickle implicitly set to true
# # restore np.load for future normal usage
np.load = np_load_old

WaysList=[]  

Start_Point=Map.Points((0,0),Map.Ways(MapNp["ObstacleList"]))
End_Point=Map.Points((0,0),Map.Ways(MapNp["ObstacleList"]))


def main():
    #Class Ways work with list not np arrays
    for way in MapNp["Paths"]:
        WaysList.append(way)
    

    Visualization=Visual(image,Map.Ways(MapNp["ObstacleList"])) 
    cv2.imshow("image",image)
    while True:
        cv2.setMouseCallback("image",Visualization.click_event)
        key=cv2.waitKey(1)
        if key==27:
            cv2.destroyAllWindows()
            break

class Visual():
    def __init__(self,image,ways):
        self.Image=image
        self.Ways=ways
        self.Ways.Path_List=[]
    
    def click_event(self,event,x,y,flag,param):
        global Start_Point,End_Point,WaysList,interfacecounter
        image_copy=copy.copy(self.Image)
        if event==cv2.EVENT_LBUTTONDOWN:
          
            self.Ways.Path_List=WaysList.copy()
            #Copies used for resetting on every click
            Start_Point.Coord=(x,y)
            Start_Point.AppendPointsToMap(self.Ways)
            End_Point.AppendPointsToMap(self.Ways)
        elif event==cv2.EVENT_RBUTTONDOWN:
           
            self.Ways.Path_List=WaysList.copy()
            End_Point.Coord=(x,y)
            Start_Point.AppendPointsToMap(self.Ways)
            End_Point.AppendPointsToMap(self.Ways)

        self.drawlines(image_copy,self.Ways.Path_List,0,0,255,1)
        


        self.DijkstrasAlgorithm(image_copy,Start_Point,End_Point)
               
    def drawlines(self,image,GivenLines=[],Blue=0,Green=0,Red=0,Thickness=1):
        for line in GivenLines:
            print("line",line)
            start=(int(line[0][0]),int(line[0][1]))
            end=(int(line[1][0]),int(line[1][1]))
            cv2.line(image,start,end,(Blue,Green,Red),Thickness)
            cv2.circle(image,start,1,(255,255,0),-1)
    def drawcircle(self,image,GivenPoints,Radius,Blue,Green,Red,Thichkness):
        cv2.circle(image,GivenPoints,Radius,(Blue,Green,Red),Thichkness)
    
    def DijkstrasAlgorithm(self,image_copy,Start_Point,End_Point):
        graph=PlanningAlgorithms.Graph_d()
        for point in self.Ways.Path_List:
            graph.AddEdges(point[0],point[1],point[2])
        path,path_cost=graph.CalculatePath(graph,Start_Point.Coord,End_Point.Coord)
        if not path=="Route Not Possible":
            self.drawlines(image_copy,path,255,0,0,4)
            
        else:
            self.drawcircle(image_copy,Start_Point.Coord,4,0,255,255,-1)
            self.drawcircle(image_copy,End_Point.Coord,4,0,255,255,-1)
        path_array = np.array(path, dtype=object) # veya np.asarray(path, dtype=object)
        np.savez("Paths",path_points=path_array)
        
        print("path",path,path_cost)
        
        cv2.imshow("image",image_copy)
        









if __name__ == "__main__":
    main()
    




