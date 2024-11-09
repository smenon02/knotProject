from helpers.load_data import *
from helpers.intersections import *
from plot import *
from helpers.traversal import *
def main():
    coords = load_coordinates()
    rotation_axis = 'x'
    rotation_angle = 90

    apply_rotation_matrix(coords, rotation_axis, rotation_angle)
    intersections, undercrossings = find_intersections(coords)
    graph = build_graph(coords, intersections)
    print(graph)
    plot(coords, intersections)

if __name__ == '__main__':
    main()