from shapely.geometry import LineString
from collections import defaultdict
from collections import deque
import math
def project_point_2D(coord):
    return tuple([coord[0], coord[1]])
def build_graph(coordinates, intersections):
    graph = defaultdict(list)
    segments = []
    for i in range(len(coordinates) - 1):
        segment = LineString([coordinates[i], coordinates[i + 1]])
        segments.append((segment, coordinates[i], coordinates[i + 1]))

    for segment, start, end in segments:
        start = project_point_2D(tuple(start))
        end = project_point_2D(tuple(end))
        graph[start].append(end)
        graph[end].append(start)

    for intersection in intersections:
        start1 = project_point_2D(intersection.l1.coords[0])
        end1 = project_point_2D(intersection.l1.coords[1])

        start2 = project_point_2D(intersection.l2.coords[0])
        end2 = project_point_2D(intersection.l2.coords[1])

        intersection_point = intersection.pt.coords[0]
        assert(isinstance(start1, tuple))
        assert(isinstance(intersection_point, tuple))

        graph[start1].append(intersection_point)
        graph[intersection_point].append(start1)
        graph[end1].append(intersection_point)
        graph[intersection_point].append(end1)
        graph[start2].append(intersection_point)
        graph[intersection_point].append(start2)
        graph[end2].append(intersection_point)
        graph[intersection_point].append(end2)
    return graph

def construct_line(pt1,pt2):
    x1 = pt1[0]
    y1 = pt1[1]

    x2 = pt2[0]
    y2 = pt2[1]
    return LineString([(x1, y1), (x2, y2)])

def build_lines(coords):
    idx1=0
    idx2=1
    lines=[]
    while(idx2 < len(coords)):
        lines.append(construct_line(project_point_2D(coords[idx1]),project_point_2D(coords[idx2])))
        idx1+=1
        idx2+=1
    return lines

def find_loop(lines, intersection, undercrossings):
    l1 = intersection.l1
    l2 = intersection.l2
    idx = lines.index(l1)
    current_line = l1
    loop = []
    while current_line != l2:
        if (current_line in undercrossings and len(loop) != 0) or idx == len(lines)-1:
            return None
        loop.append(current_line)
        idx += 1
        current_line = lines[idx]
    start_line_start_coords = intersection.pt.coords[0]
    start_line = LineString([(start_line_start_coords[0], start_line_start_coords[1]), (loop[0].coords[1][0],loop[0].coords[1][1])])
    loop.pop(0)
    loop.insert(0, start_line)
    final_line_start_coords = l2.coords[0]
    final_line_end_coords = intersection.pt.coords[0]
    final_line = LineString([(final_line_start_coords[0], final_line_start_coords[1]), (final_line_end_coords[0], final_line_end_coords[1])])
    loop.append(final_line)
    return loop

def foreground_loops(lines, intersections, undercrossings):
    foregrounds=[]
    for int in intersections:
        int_loop = find_loop(lines, int, undercrossings)
        if int_loop is not None:
            foregrounds.append(int_loop)
    return foregrounds