from shapely.geometry import LineString

def detect_foreground_loops_and_overcrossings(coordinates):
    """
    Detects foreground loops and overcrossing segments in a 2D projection by
    identifying intersections and checking if loops can be formed without undercrossings.
    This version collects the coordinates involved in detected loops.
    """

    def project_to_2d(point):
        return point[0], point[1]

    loops, overcrossings = [], []
    loop_points = []  # To store coordinates involved in detected loops
    n = len(coordinates)
    line_segments = []

    # Create line segments from the coordinates
    for i in range(n - 1):
        p1 = project_to_2d(coordinates[i])
        p2 = project_to_2d(coordinates[i + 1])
        line_segments.append(LineString([p1, p2]))

    # Check for intersections between all non-adjacent segments
    for i in range(len(line_segments) - 1):
        for j in range(i + 2, len(line_segments)):
            if abs(i - j) == 1:
                continue  # Skip consecutive segments

            segment1 = line_segments[i]
            segment2 = line_segments[j]

            # Check if segments intersect
            if segment1.intersects(segment2):
                overcrossings.append((i, j))

                # Perform a traversal to see if a loop can be formed
                visited = set()
                stack = [(i, 0), (j, 0)]  # Start from both intersecting segments
                valid_loop_found = False

                while stack:
                    current_segment, depth = stack.pop()

                    # Check if we've looped back to the intersection
                    if depth > 0 and (current_segment == i or current_segment == j):
                        valid_loop_found = True
                        break

                    # Mark the segment as visited
                    visited.add(current_segment)

                    # Explore all other segments
                    for k in range(len(line_segments)):
                        if k in visited or abs(current_segment - k) == 1:
                            continue  # Skip already visited or consecutive segments

                        # Check if current segment intersects with k
                        if segment1.intersects(line_segments[k]) or segment2.intersects(line_segments[k]):
                            stack.append((k, depth + 1))

                if valid_loop_found:
                    loops.append((i, j))
                    # Collect the coordinates involved in the loop
                    loop_points.append((coordinates[i][0], coordinates[i][1]))
                    loop_points.append((coordinates[j][0], coordinates[j][1]))

                    # To avoid duplicate points, add all points in the loop traversal
                    for k in range(len(coordinates) - 1):  # Ensure k + 1 is within bounds
                        if k in (i, j):
                            continue
                        # Check if segment k intersects with segment1 or segment2
                        if segment1.intersects(LineString([project_to_2d(coordinates[k]), project_to_2d(coordinates[k + 1])])):
                            loop_points.append((coordinates[k][0], coordinates[k][1]))

    print("Detected loops at segments:", loops)
    print("Coordinates involved in detected loops:", loop_points)
    return loops, overcrossings, loop_points
