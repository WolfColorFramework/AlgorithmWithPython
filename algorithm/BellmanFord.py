"""
BellmanFord算法
可以处理负边
循环所有边，计算最短值
"""
import math

from algorithm.Edge import Edge
from algorithm.Vertex import Vertex


class BellmanFord:

    def __init__(self, graph, vertex):
        self.__bellman_ford(graph, vertex)

        for vertex in graph:
            print(f"{vertex.name} {vertex.distance} {vertex.pre.name if vertex.pre else 'None'}")

        pass

    def __bellman_ford(self, graph, vertex):
        vertex.distance = 0

        count = len(graph) - 1

        while True:
            for vertex in graph:
                for edge in vertex.edges:  # 遍历所有的边

                    if count == 0:
                        if vertex.distance != math.inf and vertex.distance + edge.weight < edge.linked.distance:  # 启点距离+终点距离<当前边的距离
                            raise Exception("负权回路")
                        else:
                            return
                    elif vertex.distance != math.inf and vertex.distance + edge.weight < edge.linked.distance:  # 启点距离+终点距离<当前边的距离
                        edge.linked.distance = vertex.distance + edge.weight
                        edge.linked.pre = vertex
            count -= 1

        pass

    pass


if __name__ == "__main__":
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")

    v1.edges = [Edge(v2, 2), Edge(v3, 1)]
    v2.edges = [Edge(v3, -2)]
    v3.edges = [Edge(v4, 1)]
    v4.edges = []

    graph = [v1, v2, v3, v4]

    bellman_ford = BellmanFord(graph, v1)

    pass
