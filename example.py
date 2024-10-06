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
from foreground import *
import random
def main():
    rotation_axis = 'y'
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
    undercrossing_map = create_undercrossing_map(connected_alpha_coords)
    intersections, coonected_alpha_coords_with_intersections = find_intersections(connected_alpha_coords)
    define_crossings(intersections, undercrossing_map)
    foreground_loops = detect_loops(connected_alpha_coords, intersections, undercrossing_map)
    print(foreground_loops)
    plot(connected_alpha_coords, intersections)

if __name__ == "__main__":
    main()


# 1. Create a map with keys=line segments and values=boolean based on whether the line segment contains an under-crosssing
#     -initialize all keys to be true
#     -when second point found, set value of L2=False
# 2. Map each line segment to the intersection points it crosses
# 2. Create an Intersection class:
#     1. Intersection point
#     2. L1
#     3. L2
#     4. over or under crossing
# all_foreground_loops=[]
# for each intersection point:
#     p1=first point of l1
#     p2=second point of l1
#     foreground_loop = True
#     path_taken = []
#     while p2 != intersection point:
#         line = p1 --> p2
#         if line == L2:
#             p2 = intersection point
#             for all intersection_points except starting_intersection:
#                 if intersection_point.L2 = p1p2:
#                     foreground_loop = False
#                     break
#         elif map of lines to overcrossings[line] == False:
#             foreground_loop = False
#             break
#         else:
#             path_taken.append(line)
#             p1 = p2
#             p2 = point after p2
#     if foreground_loop:
#         all_foreground_loops.append(path_taken)

