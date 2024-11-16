import random
import math
from math import radians
from math import sin
from math import cos
import numpy as np
def load_coordinates():
    # random.seed(50)
    # num_coords = 10 #Speicifes number of coordinates to randomly generate
    # coordinates = []
    # for i in range(num_coords):
    #     coordinates.append([random.randint(1,10),
    #                                    random.randint(1,10),
    #                                    random.randint(1,10)])
    # return coordinates
    coordinates = [
        [0, 0, 0],  # Point 0
        [4, 2, 0],  # Point 1
        [5, 5, 0],  # Point 2
        [2, 6, 0],  # Point 3 (This point intersects the lines)
        [1, 4, 0],  # Point 4 (Creates a loop)
        [3, 3, 0],  # Point 5 (Another distinct point)
        [6, 1, 0],  # Point 6 (Crossing segment)
        [7, 4, 0],  # Point 7
        [3, 0, 0],  # Point 8
        [0, 7, 0]  # Point 9 (This point completes the loop)
    ]
    return coordinates
def create_rotation_matrix(axis, angle):
    # Convert from degrees to radians
    angle = radians(angle)
    # Creates rotation matrix according to specified axis
    if axis.lower() == "x":
        return np.array([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
    elif axis.lower() == "y":
        return np.array([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ])
    elif axis.lower() == "z":
        return np.array([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])
    else:
        return ("Specify x,y, or z axis for rotation matrix")

# Requires: chain coordinates, axis of rotation, angle of rotation(degrees)
# Modifies: alpha chain coordinates
# Effects: Applies a specified rotation matrix to a set of alpha chain coordinates
def apply_rotation_matrix(chain, rotation_axis, rotation_angle):
    # creates rotation matrix
    rotation_matrix = create_rotation_matrix(rotation_axis, rotation_angle)
    # Iterate through each set of coordinates in chain
    for i in range(len(chain)):
        # Isolate coordinate set for given iterations
        coord_set = chain[i]
        # Applies dot product of coordinate set and rotation matrix
        coord_set = np.dot(rotation_matrix, coord_set)
        # Replaces values in original coordinate set with dot product result
        chain[i][0] = round(coord_set[0], 3)
        chain[i][1] = round(coord_set[1], 3)
        chain[i][2] = round(coord_set[2], 3)
