from shapely import coordinates
from shapely.geometry import LineString, Point

def detect_endpoints(coordinates):
  endpoints = []
  for i in range(len(coordinates)):
    endpoints.append(True if i == 0 or i == len(coordinates)-1 else False)
  return endpoints

class Projection:
  def __init__(self, object):
    if isinstance(object, LineString):
      self.line = LineString([(x,y,0) for x,y,z in object.coords])
    else:
      self.coords = Point(coordinates[0], coordinates[1], 0)

  def project_2D(self):
    if hasattr(self, 'coords'):
      return self.coords
    else:
      return self.line