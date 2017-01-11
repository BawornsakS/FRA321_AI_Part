import math

from implementation import *

class Node:
    def __init__(self, name = None, neighbors = None, x = None, y = None):
        self.name = name
        self.neighbors = neighbors
        self.x = x
        self.y = y

    def dist(self, b):
        return math.sqrt(math.pow(self.x - b.x, 2) + math.pow(self.y - b.y, 2))
