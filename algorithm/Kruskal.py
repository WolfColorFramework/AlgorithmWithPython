"""
最小生成树
"""
from algorithm.Edge2 import Edge2
from algorithm.Vertex import Vertex
from algorithm.DisjointSet import DisjointSet
import queue


class Kruskal:

    def __init__(self):
        pass

    def kruskal(self, size, queue):

        result = []
        set = DisjointSet()
        while len(result) < size - 1:
            edge = queue.get()
            i = set.find(edge.start)
            j = set.find(edge.end)
            if i != j:
                result.append(edge)
                set.union(i, j)
                pass

        pass

    pass


if __name__ == "__main__":
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")
    v5 = Vertex("v5")
    v6 = Vertex("v6")
    v7 = Vertex("v7")

    vertices = [v1, v2, v3, v4, v5, v6, v7]

    pq = queue.PriorityQueue()
    pq.put(Edge2(vertices, 0, 1, 2))
    pq.put(Edge2(vertices, 0, 2, 4))
    pq.put(Edge2(vertices, 0, 3, 1))
    pq.put(Edge2(vertices, 1, 3, 3))
    pq.put(Edge2(vertices, 1, 4, 10))
    pq.put(Edge2(vertices, 2, 3, 2))
    pq.put(Edge2(vertices, 2, 5, 5))
    pq.put(Edge2(vertices, 3, 4, 7))
    pq.put(Edge2(vertices, 3, 5, 8))
    pq.put(Edge2(vertices, 3, 6, 4))
    pq.put(Edge2(vertices, 4, 6, 6))
    pq.put(Edge2(vertices, 5, 6, 1))

    kruskal = Kruskal()



    pass
