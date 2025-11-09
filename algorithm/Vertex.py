"""
图的顶点
"""


class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = list()
        self.visited = False
        self.in_degree = 0


if __name__ == "__main__":
    pass
