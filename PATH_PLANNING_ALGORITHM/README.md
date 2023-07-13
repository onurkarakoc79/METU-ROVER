# Computer Vision Rover Path Planning

This is a path planning code for a rover developed using Python. The code utilizes the Dijkstra's algorithm to find the shortest path between a given start point and an end point, considering obstacles in the environment. It is designed to work with images as input for computer vision applications.

## Features

- Calculation of the shortest path using Dijkstra's algorithm
- Handling of obstacles defined as convex shapes
- Visualization of the path on an input image
- Integration with computer vision applications

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository to your local machine:
git clone <https://github.com/onurkarakoc79/METU-ROVER.git)>

2. Install requirement libraries
pip install -r requirements.txt

Usage
Configure the map and obstacle settings in the main() function of Map.py file.
Prepare an input image of the map on which you want to perform path planning.
Run the path planning code:
shell
Copy code

python3 Map.py

After execute Map.py file you dont need to execute everytime unless map were changed.
After that execute VisualwithClick.py file
Copy code

python3 VisualwithClick.py

Click on the image to specify the start and end points.
The calculated path will be displayed on the image.
You can close the window with ESC button.


![Alt text]()

