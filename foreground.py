from utils import *
def find_coordinate_index(coords, coordinate):
    coordinate = list(coordinate)
    for i in range(len(coords)):
        if coords[i][0] == coordinate[0] and coords[i][1] == coordinate[1]:
            return i
def detect_loops(coords, intersections, undercrossings_map):
    all_foreground_loops=[]
    for intersection in intersections:
        intersection_index = find_coordinate_index(coords, intersection.point.coords[0])
        p1_index = find_coordinate_index(coords, intersection.l1.coords[0])
        p2_index = p1_index + 1
        foreground_loop = True
        path_taken = []
        while p2_index != intersection_index and p2_index < len(coords):
            p1 = coords[p1_index]
            p2 = coords[p2_index]
            line = LineString([p1, p2])
            if Projection(line).project_2D() == intersection.l2:
                p2 = intersection.point
                p2_index = intersection_index
                line = LineString([p1, p2])
                for other_intersection in intersections:
                    if intersection.l2 == line and other_intersection != intersection:
                        foreground_loop = False
                        break
            elif undercrossings_map[line]:
                foreground_loop = False
                break
            else:
                path_taken.append(line)
                p1_index = p2_index
                p2_index += 1
        if foreground_loop:
            all_foreground_loops.append(path_taken)

