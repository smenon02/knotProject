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

def shortest_loops(cycle_map):
    shortest_cycles = {}
    for node,path in cycle_map.items():
        visited = {}
        min_cycle = None
        for i, current in enumerate(path):
            if current in visited:
                start_idx = visited[current]
                cycle = path[start_idx:i + 1]
                if min_cycle is None or len(cycle) < len(min_cycle):
                    min_cycle = cycle
            visited[current] = i
        shortest_cycles[node] = min_cycle if min_cycle else []
    return shortest_cycles

def euclidien_distance(coord1, coord2):
    x1=coord1[0]
    y1=coord1[1]
    x2=coord2[0]
    y2=coord2[1]
    return math.sqrt((x1 - x2)**2 + (y1-y2)**2)
def find_cycle(graph):
    cycles = {}
    visited = {}
    def dfs(current, start, visited, path):

        visited[current] = True
        path.append(current)
        for neighbor in graph[current]:
            if neighbor == start and len(path) > 2:
                return path + [start]
            elif not visited.get(neighbor, False):
                result = dfs(neighbor, start, visited, path)
                if result:
                    return result

        path.pop()
        visited[current] = False
        return None

    for node in graph:
        visited = {}
        cycle = dfs(node, node, visited, [])
        if cycle:
            cycles[node] = cycle

    return shortest_loops(cycles)

def construct_line(pt1,pt2):
    x1 = pt1[0]
    y1 = pt2[1]

    x2 = pt2[0]
    y2 = pt2[1]
    return LineString([(x1, y1), (x2, y2)])
def foregrounds(cycles, undercrossings, intersections):
    foreground_loops=[]
    for intersection in intersections:
        foreground_found = True
        intersection = tuple([intersection.pt.coords[0][0], intersection.pt.coords[0][1]])
        cycle = cycles[intersection]
        cycle_lines=[]
        for i in range(len(cycle)-2):
            cycle_lines.append(construct_line(cycle[i], cycle[i+1]))
        for line in cycle_lines:
            for under_line in undercrossings:
                if line.distance(under_line) < .0001:
                    foreground_found = False
        if foreground_found:
            foreground_loops.append(cycle)
    return foreground_loops



