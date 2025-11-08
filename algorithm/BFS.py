"""
深度优先搜索
"""
from algorithm.Edge import Edge
from algorithm.Vertex import Vertex
from collections import deque


class BFS:

    def bfs(self, vertex):
        queue = deque()
        queue.append(vertex)
        vertex.visited = True
        while len(queue) > 0:
            v = queue.popleft()
            print(f"{v.name}")
            for edge in v.edges:
                if not edge.linked.visited:
                    edge.linked.visited = True
                    queue.append(edge.linked)


    pass


if __name__ == "__main__":
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")
    v5 = Vertex("v5")
    v6 = Vertex("v6")

    v1.edges = [Edge(v3), Edge(v2), Edge(v6)]
    v2.edges = [Edge(v4)]
    v3.edges = [Edge(v4), Edge(v6)]
    v4.edges = [Edge(v5)]
    v5.edges = []
    v6.edges = [Edge(v5)]

    bfs = BFS()
    bfs.bfs(v1)

    pass
