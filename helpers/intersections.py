from shapely.geometry import LineString
from shapely.geometry import Point
from itertools import combinations
class Intersection:
    def __init__(self, l1, l2, crossing_in, pt):
        self.l1 = l1
        self.l2 = l2
        self.crossing_type = crossing_in
        self.pt = pt

def interpolate_z(p1,p2,t):
    return p1[2] + t * (p2[2]-p1[2])

def is_overcrossing(l1, l2):
    l1_start = l1.coords[0]
    l1_end = l1.coords[1]
    l2_start = l2.coords[0]
    l2_end = l2.coords[1]

    l1_2d = LineString([(l1_start[0], l1_start[1]), (l1_end[0], l1_end[1])])
    l2_2d = LineString([(l2_start[0], l2_start[1]), (l2_end[0], l2_end[1])])

    intersection_point = l1_2d.intersection(l2_2d)

    t1 = l1_2d.project(intersection_point) / l1_2d.length
    t2 = l2_2d.project(intersection_point) / l2_2d.length

    z1 = interpolate_z(l1_start, l1_end, t1)
    z2 = interpolate_z(l2_start, l2_end, t2)

    return z1 > z2

def project_line_2D(line):
    x1 = line.coords[0][0]
    y1 = line.coords[0][1]

    x2 = line.coords[1][0]
    y2 = line.coords[1][1]

    return LineString([(x1, y1), (x2, y2)])
def find_intersections(coords):
    line_segments = []
    intersections = []
    undercrossing_lines = []
    overcrossing_lines = []
    for i in range(len(coords)-1):
        x1 = coords[i][0]
        y1 = coords[i][1]
        z1 = coords[i][2]

        x2 = coords[i+1][0]
        y2 = coords[i+1][1]
        z2 = coords[i + 1][2]
        line_segments.append(LineString([(x1,y1,z2),(x2,y2,z2)]))

    for i in range(len(line_segments)-1):
        for j in range(i+1, len(line_segments)):
            l1 = line_segments[i]
            l2 = line_segments[j]

            l1_2d = project_line_2D(l1)
            l2_2d = project_line_2D(l2)
            if l1_2d.intersects(l2_2d) and not l1_2d.intersection(l2_2d).is_empty:
                under_line = l2_2d if is_overcrossing(l1,l2) else l1_2d
                over_line = l1_2d if under_line is l2_2d else l2_2d
                crossing_type = 'over' if is_overcrossing(l1,l2) else 'under'
                point = l1_2d.intersection(l2_2d)
                if point.coords[0] != l1_2d.coords[1] and point.coords[0] != l2_2d.coords[0]:
                    #point = Point([round(point.coords[0][0],1), round(point.coords[0][0],1)])
                    intersections.append(Intersection(l1_2d, l2_2d, crossing_type, point))
                    undercrossing_lines.append(under_line)
                    overcrossing_lines.append(over_line)
    return intersections, undercrossing_lines, overcrossing_lines


