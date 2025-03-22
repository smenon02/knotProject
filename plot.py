
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
from utils import *
#Requires: List of LineString Objects, List of intersection information
#Modifies:
#Effects: Creates a 2D plot with defined crossing types for a set of lines
def plot(coordinates, foregrounds, overcrossings):
    fig, ax = plt.subplots()
    x_values = [x for x, y, z in coordinates]
    y_values = [y for x, y, z in coordinates]
    endpoints = detect_endpoints(coordinates)

    # Plot the points
    plt.plot(x_values, y_values, color='black')

    # for intersection in intersections:
    #     x = intersection.pt.coords[0][0]
    #     y = intersection.pt.coords[0][1]
    #     plt.plot(x, y, 'o', color='black')
    # for intersection in intersections:
    #     xs1, ys1 = zip(*[(x, y) for x, y, z in intersection.l1.coords])
    #     ax.plot(xs1, ys1, color='black', zorder=2, linewidth=3)  # Over line
    for line in overcrossings:
        x,y = line.xy
        plt.plot(x, y, label="LineString", color='gold')

    for fore in foregrounds:
        for line in fore:
            x,y = line.xy
            plt.plot(x, y, label="LineString", color='blue')  # Plot the line
            plt.scatter(x, y, color='blue', label="Coordinates", zorder=5)  # Highlight points

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Show the plot
    plt.show()
