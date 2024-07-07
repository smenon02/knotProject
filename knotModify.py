import math
from math import radians
from math import sin
from math import cos
import numpy as np
from shapely.geometry import LineString, Point
#Requires: Axis of rotation, angle(degrees)
#Modifies:
#Effects: Helper function that takes in a specified rotation axis and angle and returns a corresponding rotation matrix
def create_rotation_matrix(axis, angle):
  #Convert from degrees to radians
  angle=radians(angle)
  #Creates rotation matrix according to specified axis
  if axis.lower()=="x":
    return np.array([
              [1, 0, 0],
              [0, cos(angle), -sin(angle)],
              [0, sin(angle), cos(angle)]
              ])
  elif axis.lower()=="y":
    return np.array([
              [cos(angle), 0, sin(angle)],
              [0, 1, 0],
              [-sin(angle), 0, cos(angle)]
              ])
  elif axis.lower()=="z":
      return np.array([
              [cos(angle), -sin(angle), 0],
              [sin(angle), cos(angle), 0],
              [0, 0, 1]
              ])
  else:
      return("Specify x,y, or z axis for rotation matrix")

#Requires: chain coordinates, axis of rotation, angle of rotation(degrees)
#Modifies: alpha chain coordinates
#Effects: Applies a specified rotation matrix to a set of alpha chain coordinates
def apply_rotation_matrix(chain, rotation_axis, rotation_angle):
    #creates rotation matrix
    rotation_matrix = create_rotation_matrix(rotation_axis, rotation_angle)
    #Iterate through each set of coordinates in chain
    for i in range(len(chain)):
        #Isolate coordinate set for given iterations
        coord_set = chain[i]
        #Applies dot product of coordinate set and rotation matrix
        coord_set = np.dot(rotation_matrix,coord_set)
        #Replaces values in original coordinate set with dot product result
        chain[i][0]=coord_set[0]
        chain[i][1]=coord_set[1]
        chain[i][2]=coord_set[2]

