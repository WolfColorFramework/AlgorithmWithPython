"""
图的边
"""


class Edge:
    def __init__(self, vertex):
        self.linked = vertex
        self.weight = 0
