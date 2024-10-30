from helpers.load_data import *
from helpers.loop_detection import *
from helpers.projection import *
from helpers.plotting import *
from helpers.rotation import *

def main():
    # Step 1: Load 3D coordinates
    coordinates = load_coordinates()

    rotation_axis = 'X'
    rotation_angle = 0
    apply_rotation_matrix(coordinates, rotation_axis, rotation_angle)

    # Step 2: Detect foreground loops
    loops, overcrossings, loop_points = detect_foreground_loops_and_overcrossings(coordinates)


    # Step 3: Project coordinates to 2D
    projected_coordinates = project_to_2d(coordinates)

    # Step 4: Plot the structure with foreground loops highlighted
    plot_structure_with_loops(projected_coordinates, loops, overcrossings)


if __name__ == "__main__":
    main()
