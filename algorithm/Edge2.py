"""
图的边
"""


class Edge2:
    def __init__(self, vertexes, start, end, wight=0):
        self.vertexes = vertexes
        self.start = start
        self.end = end
        self.weight = wight

    def __lt__(self, other):
        # 定义优先级比较规则：数值越小优先级越高
        return self.weight < other.weight

    def __repr__(self):
        return f"Edge2({self.vertexes[self.start].name}<->{self.vertexes[self.end].name}, {self.weight})"
