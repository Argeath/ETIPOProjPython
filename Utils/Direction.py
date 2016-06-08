import numpy as np


class Direction:
    NORTH = np.array([0, -1])
    SOUTH = np.array([0, 1])
    WEST = np.array([-1, 0])
    EAST = np.array([1, 0])
    NONE = np.array([0, 0])

    all = [NORTH, SOUTH, WEST, EAST]
