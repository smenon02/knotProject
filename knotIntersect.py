from shapely.geometry import LineString, Point
#Requires: set of coordinates
#Modifies:
#Effects: Takes in a list of coordinates and returns a list of corresponding LineString objects
def coordinates_to_lines(coords):
  #Initializes empty list to stroe LineString objects
  Lines=[]
  #Iterate through all coordinates
  for i in range(len(coords)-1):
    #Take x,y,z coordinates from set i
    x1=coords[i][0]
    y1=coords[i][1]
    z1=coords[i][2]

    #Take x,y,z coordinates from set i+1
    x2=coords[i+1][0]
    y2=coords[i+1][1]
    z2=coords[i+1][2]
    #Create LineString object from connected coordinate sets i and i+1
    Lines.append(LineString([[x1,y1,z1],[x2,y2,z2]]))
  return Lines

#Requires: LineString object
#Modifies:
#Effects:Helper function that projects a LineString object from 3D --> 2D
def project_line_to_2D(line):
  #Extract coordinates from LineString
  coords=list(line.coords)

  #Initialize x,y, and z coordinates from first set of coordinates in LineString. Set z=0 for 2D projection.
  x1=coords[0][0]
  y1=coords[0][1]
  z1=0

  # Initialize x,y, and z coordinates from second set of coordinates in LineString. Set z=0 for 2D projection.
  x2=coords[1][0]
  y2=coords[1][1]
  z2=0

  #Return LineString objct corresponding to 2D projected coordinates
  return LineString([[x1,y1,z1],[x2,y2,z2]])

#Requires: set of coordinates
#Modifies:
#Effects: Takes in a set of coordinates and returns a map of intersections. In the map:
  #Keys-Intersection points
  #Values-List of 2 LineString objects corresponding to the lines at which the intersection occurs
def find_intersections(coords):
    #Converts coordinates to LineString objects
    lines=coordinates_to_lines(coords)
    #Initializes empty map to hold intersection information
    intersections_mapped={}
    #Iterate through set of lines
    for i in range(0,len(lines)-1):
      #Isolate LineObject for iteration i
      l1=lines[i]
      #Project line to 2D
      l1_2D=project_line_to_2D(l1)
      #Isolate points from 2D projected line
      l1_2D_points=list(l1_2D.coords)
      #Iterate through all lines starting from line i
      for j in range(i+1, len(lines)):
        #Isolate LineObject for iteration j
        l2=lines[j]
        #Project line to 2D
        l2_2D=project_line_to_2D(l2)
        #Isolate points from 2D projected line
        l2_2D_points=list(l2_2D.coords)

        #If l1 intersects l2 and l1 and l2 don't share a common point
        if l1_2D.intersects(l2_2D) and not (any(i in l1_2D_points for i in l2_2D_points)):
          #Define intersection point
          intersect = l1_2D.intersection(l2_2D)
          #Mappings intersection point to lines where intersection occurs
          intersections_mapped[intersect] = [l1,l2]
    return intersections_mapped

#Requires: LineString object, intersection point
#Modifies:
#Effects: Helper function that calculates the interpolated z-value at a given intersection point on a 3D line segment.
#Used for determining over/under-crossings.
def interpolate_z(line, xy_point):
  # Extract the list of coordinates from the line object
  coords = list(line.coords)

  # Iterate through each segment in the line
  for i in range(len(coords) - 1):
    # Get the coordinates of the current segment's start and end points
    (x1, y1, z1) = coords[i]
    (x2, y2, z2) = coords[i + 1]

    # Check if the xy_point lies within the x and y bounds of the current segment
    if (x1 <= xy_point.x <= x2 or x2 <= xy_point.x <= x1) and (y1 <= xy_point.y <= y2 or y2 <= xy_point.y <= y1):
      # Calculate the interpolation factor t based on the x or y values
      if x1 != x2:
        t = (xy_point.x - x1) / (x2 - x1)
      else:
        t = (xy_point.y - y1) / (y2 - y1)

      # Interpolate the z-value using the factor t
      z = z1 + t * (z2 - z1)

      # Return the interpolated z-value
      return z

  # If the point does not lie within any segment, return None
  return None

#Requires: List of intersection information
#Modifies:
#Effects: Defines crossing types for each intersection in an input. Returns a list of lists, with each inner list containings 3 elements.
  #Elt 1: Intersection Point
  #Elt 2: List of 2 LineString objects where intersection occurs
  #Elt 3: Crossing Type(ie:"over", "under" etc)
def define_crossings(intersections):
  #Initializes empty list to store crossing type information
  full_mapping=[]
  #Iterate through each intersection
  for intersection in intersections:
    #Finds interpolated z values for both lines in intersection
    z1=interpolate_z(intersections[intersection][0], intersection)
    z2=interpolate_z(intersections[intersection][1], intersection)

    #If both interpolated z values exist
    if z1 is not None and z2 is not None:
      #Definition of over-crossing(ie: Line 1 crosses over Line 2)
      if z1 > z2:
          #print(f"Line 1 is over Line 2 at {intersection} with Z1 = {z1} and Z2 = {z2}")
          #Adds list containing over-crossing information to full set
          full_mapping.append([intersection, [intersections[intersection][0],intersections[intersection][1]], "over"])
          #full_mapping.append([intersection, [intersections[intersection][0],intersections[intersection][1]], "under"])
      # Definition of under-crossing(ie: Line 1 crosses under Line 2)
      elif z1 < z2:
          #print(f"Line 1 is under Line 2 at {intersection} with Z1 = {z1} and Z2 = {z2}")
          # Adds list containing under-crossing information to full set
          full_mapping.append([intersection, [intersections[intersection][0],intersections[intersection][1]], "under"])
          #full_mapping.append([intersection, [intersections[intersection][0],intersections[intersection][1]], "over"])
  return full_mapping
