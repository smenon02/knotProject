def detect_endpoints(coordinates):
  endpoints = []
  for i in range(len(coordinates)):
    endpoints.append(True if i == 0 or i == len(coordinates)-1 else False)
  return endpoints
