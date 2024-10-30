# plotting.py

import matplotlib.pyplot as plt
from shapely.geometry import LineString


def plot_structure_with_loops(coordinates, loops, overcrossings):
    """
    Plots the 2D projection of the protein structure with detected loops and overcrossings.
    """
    print(coordinates)
    # Project coordinates to 2D
    x = [point[0] for point in coordinates]
    y = [point[1] for point in coordinates]

    plt.figure(figsize=(10, 8))

    # Plot each line segment
    for i in range(len(coordinates) - 1):
        plt.plot(x[i:i + 2], y[i:i + 2], color='black', linewidth=1)  # Default black lines

    # Highlight loops with thicker lines
    for (i, j) in loops:
        plt.plot(x[i:j + 1], y[i:j + 1], color='red', linewidth=3, label='Loop')  # Red for loops

    # Highlight overcrossings
    # for (i, j) in overcrossings:
    #     plt.plot(x[i:j + 1], y[i:j + 1], color='blue', linewidth=2, linestyle='dashed',
    #              label='Overcrossing')  # Dashed blue lines

    plt.title('2D Projection of Protein Structure with Loops and Overcrossings')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid()
    plt.axis('equal')

    # Create a legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.show()
