
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
from utils import *
#Requires: List of LineString Objects, List of intersection information
#Modifies:
#Effects: Creates a 2D plot with defined crossing types for a set of lines
def plot(coordinates):
    fig, ax = plt.subplots()
    x_values = [x for x, y, z in coordinates]
    y_values = [y for x, y, z in coordinates]
    endpoints = detect_endpoints(coordinates)

    # Plot the points
    plt.plot(x_values, y_values, color='black')

    # Label each point with its order
    for i, (x, y, z) in enumerate(coordinates):
        plt.text(x, y, f'{i}', fontsize=15, ha='right')
        if endpoints[i]:
            plt.scatter(x,y,color='red', s=100)

    # for intersection in intersections:
    #     xs1, ys1 = zip(*[(x, y) for x, y, z in intersection.l1.coords])
    #     ax.plot(xs1, ys1, color='black', zorder=2, linewidth=3)  # Over line
    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Show the plot
    plt.show()
