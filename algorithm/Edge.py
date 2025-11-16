"""
图的边
"""


class Edge:
    def __init__(self, vertex, wight=0):
        self.linked = vertex
        self.weight = wight
