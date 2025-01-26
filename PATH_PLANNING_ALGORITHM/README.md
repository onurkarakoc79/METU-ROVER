# Computer Vision Rover Path Planning

This is a path planning code for a rover developed using Python. The code utilizes Dijkstra's algorithm to find the shortest path between a given start point and an endpoint, considering obstacles in the environment. It is designed to work with images as input for computer vision applications.

## Features

- Calculation of the shortest path using Dijkstra's algorithm
- Handling of obstacles defined as convex shapes
- Visualization of the path on an input image
- Integration with computer vision applications

## Prerequisites

- Python 3. x

## Installation

1. Clone the repository to your local machine:

```bash
   git clone https://github.com/onurkarakoc79/METU-ROVER.git
```

3. Install requirement libraries
pip install -r requirements.txt

Usage
Configure the map and obstacle settings in the main() function of the Map.py file.
Prepare an input image of the map on which you want to perform path planning.
Run the path planning code:
shell
Copy code

python3 Map.py

After executing the Map.py file you don't need to execute it every time unless the map was changed.
After that execute the VisualwithClick.py file
Copy code

python3 VisualwithClick.py

Click on the image to specify the start and end points.
The calculated path will be displayed on the image.
You can close the window with the ESC button.


![Alt text](https://github.com/onurkarakoc79/METU-ROVER/blob/main/PATH_PLANNING_ALGORITHM/Screenshots/Screenshot%20from%202023-07-14%2002-44-29.png)


![Alt text](https://github.com/onurkarakoc79/METU-ROVER/blob/main/PATH_PLANNING_ALGORITHM/Screenshots/Screenshot%20from%202023-07-14%2002-44-46.png)

## Contact

If you have any questions, feedback, or inquiries related to the project, feel free to reach out to me:

My personal mail: onurkarakoc79@gmail.com

                  
I appreciate your interest in my projects and look forward to collaborating with you in the fascinating field of scientific exploration and discovery.


