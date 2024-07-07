#import libraries
import numpy as np
from Bio import PDB
from shapely.ops import unary_union
from mpl_toolkits.mplot3d import Axes3D
#imports from helper files
from knotLoad import connect_4th_alphas
from knotModify import apply_rotation_matrix
from knotIntersect import find_intersections
from knotIntersect import define_crossings
from knotIntersect import coordinates_to_lines
from plot import plot_lines_and_crossings
def main():
    #Defines input file to draw protein information from
    pdb_file = "inputdata/1yve.pdb"
    #Defines axis by which rotation matrix will be applied
    rotation_axis = 'x'
    #Defines angle at which rotation matrix will be applied
    rotation_angle = 90

    #Connect every 4th alpha coordinate in input file
    connected_alpha_coords = connect_4th_alphas(pdb_file)
    #Applies rotation matrix to connectec chain of alpha carbons
    apply_rotation_matrix(connected_alpha_coords, rotation_axis, rotation_angle)
    #Creates line objects from coordinates. Used for plotting
    lines = coordinates_to_lines(connected_alpha_coords)
    #Finds intersections in 2D projection of alpha chain
    intersections = find_intersections(connected_alpha_coords)
    #Defines crossing types for each intersection.
    crossings = define_crossings(intersections)
    #Plots line objects along with defined crossings and intersections
    plot_lines_and_crossings(lines, crossings)
if __name__ == "__main__":
    main()