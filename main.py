from helpers.load_data import *
from helpers.intersections import *
from plot import *
from helpers.traversal import *
def main():
    coords = load_coordinates('inputdata/1yve.pdb')
    rotation_axis = 'x'
    rotation_angle = 90

    # apply_rotation_matrix(coords, rotation_axis, rotation_angle)
    intersections, undercrossings, overcrossings = find_intersections(coords)
    #graph = build_graph(coords, intersections)
    foregrounds = foreground_loops(build_lines(coords), intersections=intersections, undercrossings=undercrossings)
    #print(intersections)
    plot(coords, foregrounds, overcrossings)

if __name__ == '__main__':
    main()

    