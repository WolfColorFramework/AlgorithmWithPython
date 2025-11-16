"""
单元最短路径
"""
from algorithm.Edge import Edge
from algorithm.Vertex import Vertex
import heapq


class Dijkstra:

    def dijkstra(self, graph, vertex):
        vertex.distance = 0

        min_heap = [(vertex.distance, vertex) for vertex in graph]
        heapq.heapify(min_heap)  # 初始化最小堆

        while len(min_heap) > 0:
            # 选取当前最小顶点
            _, curr = heapq.heappop(min_heap)  # 弹出最小堆的元素

            # 更新当前顶点的邻居的距离
            if curr.visited is False:
                self.__update_neighbor_distance(curr, min_heap)
                curr.visited = True

            pass

        for vertex in graph:
            print(f"{vertex.name} {vertex.distance} {vertex.pre.name if vertex.pre else 'None'}")

        pass

    def __update_neighbor_distance(self, vertex, min_heap):
        for edge in vertex.edges:
            if not edge.linked.visited:
                if edge.linked.distance > vertex.distance + edge.weight:
                    edge.linked.distance = vertex.distance + edge.weight
                    edge.linked.pre = vertex
                    heapq.heappush(min_heap, (edge.linked.distance, edge.linked))  # 重新插入，使最小堆重新排序
                pass

    pass


if __name__ == "__main__":
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")
    v5 = Vertex("v5")
    v6 = Vertex("v6")

    v1.edges = [Edge(v3, 9), Edge(v2, 7), Edge(v6, 14)]
    v2.edges = [Edge(v4, 15)]
    v3.edges = [Edge(v4, 11), Edge(v6, 2)]
    v4.edges = [Edge(v5, 6)]
    v5.edges = []
    v6.edges = [Edge(v5, 9)]

    graph = [v1, v2, v3, v4, v5, v6]

    dijkstra = Dijkstra()

    dijkstra.dijkstra(graph, v1)

    pass
