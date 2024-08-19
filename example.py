#import libraries
import numpy as np
from Bio import PDB
from shapely.ops import unary_union
from mpl_toolkits.mplot3d import Axes3D
#imports from helper files
from knotLoad import *
from knotModify import *
from knotIntersect import *
from plot import *
import random
def main():
    rotation_axis = 'x'
    # Defines angle at which rotation matrix will be applied
    rotation_angle = 90
    random.seed(50)
    num_coords = 10 #Speicifes number of coordinates to randomly generate
    connected_alpha_coords = []
    for i in range(num_coords):
        connected_alpha_coords.append([random.randint(1,10),
                                       random.randint(1,10),
                                       random.randint(1,10)])
    apply_rotation_matrix(connected_alpha_coords, rotation_axis, rotation_angle)
    plot_coordinates(connected_alpha_coords)

if __name__ == "__main__":
    main()