from shapely.geometry import LineString
from collections import defaultdict
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

