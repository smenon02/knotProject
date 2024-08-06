
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
#Requires: List of LineString Objects, List of intersection information
#Modifies:
#Effects: Creates a 2D plot with defined crossing types for a set of lines
def plot_lines_and_crossings(lines, intersections):
    fig, ax = plt.subplots()

    #Iterate through each line
    for line in lines:
        #Extract 2D coordinates for line and plot
        xs, ys = zip(*[(x, y) for x, y, z in line.coords])
        ax.plot(xs, ys, color='black')

        #ax.text(status, color='black')
    #Iterate through each intersection
    for intersection, lines, status in intersections:
        #Extract lines at which intersection occurs
        line1, line2 = lines

        # Plot based on the status
        if status == 'over':
            # Line1 over Line2
            # xs2, ys2 = zip(*[(x, y) for x, y, z in line2.coords])
            # ax.plot(xs2, ys2, color='red', zorder=1)  # Under line

            xs1, ys1 = zip(*[(x, y) for x, y, z in line1.coords])
            ax.plot(xs1, ys1, color='black', zorder=2,linewidth=3)  # Over line
        elif status == "under":
            # Line1 under Line2
            # xs1, ys1 = zip(*[(x, y) for x, y, z in line1.coords])
            # ax.plot(xs1, ys1, color='red', zorder=1)  # Under line

            xs2, ys2 = zip(*[(x, y) for x, y, z in line2.coords])
            ax.plot(xs2, ys2, color='black', zorder=2,linewidth=3)  # Over line

        # Plot the intersection point
        ax.scatter(intersection.x, intersection.y, c='black', marker='o', s=20, zorder=3)

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    #plt.legend()
    plt.show()
