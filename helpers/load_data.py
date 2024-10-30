import random
def load_coordinates():
    # random.seed(50)
    # num_coords = 10 #Speicifes number of coordinates to randomly generate
    # coordinates = []
    # for i in range(num_coords):
    #     coordinates.append([random.randint(1,10),
    #                                    random.randint(1,10),
    #                                    random.randint(1,10)])
    # return coordinates
    coordinates = [
        [0, 0, 0],  # Point 0
        [4, 2, 0],  # Point 1
        [5, 5, 0],  # Point 2
        [2, 6, 0],  # Point 3 (This point intersects the lines)
        [1, 4, 0],  # Point 4 (Creates a loop)
        [3, 3, 0],  # Point 5 (Another distinct point)
        [6, 1, 0],  # Point 6 (Crossing segment)
        [7, 4, 0],  # Point 7
        [3, 0, 0],  # Point 8
        [0, 7, 0]  # Point 9 (This point completes the loop)
    ]

    return coordinates