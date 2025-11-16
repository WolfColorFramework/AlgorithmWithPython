"""
图的顶点
"""

import math


class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = list()
        self.visited = False
        self.in_degree = 0
        self.distance = math.inf
        self.pre = None

    def __lt__(self, other):
        return self.distance < other.distance


if __name__ == "__main__":
    pass
