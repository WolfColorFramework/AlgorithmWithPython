"""弗洛伊德-多源最短路径"""
import math

from algorithm.Edge import Edge
from algorithm.Vertex import Vertex


class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        pass

    def floyd_warshall(self):
        size = len(self.graph)
        dist = [[0 for _ in range(size)] for _ in range(size)]
        prev = [[Vertex(None) for _ in range(size)] for _ in range(size)]

        # 初始化
        for i in range(size):
            v = self.graph[i]
            dict = {edge.linked: edge.weight for edge in v.edges}  # edge转换为字典（key:顶点 value:权重）
            for j in range(size):
                u = self.graph[j]
                if v is u:
                    dist[i][j] = 0
                    pass
                else:
                    dist[i][j] = dict.get(u, math.inf)
                    prev[i][j] = v if dict.get(u) is not None else None
                    pass
                pass
            pass
        # self.print_dist(dist)
        # self.print_prev(prev)

        # 借路到达新的顶点
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if dist[i][k] is not math.inf and dist[k][j] is not math.inf \
                            and dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        prev[i][j] = prev[k][j]
                        pass
            # self.print_dist(dist)
        self.print_prev(prev)

        if self.detect_negative_cycle(dist):
            print("存在负环")
        else:
            self.print_dist(dist)
        pass

    def print_dist(self, dist):
        for i in range(len(dist)):
            print(f"{dist[i]}", end="\n")
        pass

    pass

    def print_prev(self, prev):

        for i in range(len(prev)):
            # print(f"{prev[i]}", end="\n")
            print(f"{list(map(lambda v: v.name if v is not None else None, prev[i]))}", end="\n")
        pass

    def detect_negative_cycle(self, dist):
        """
        检测是否存在负环 对角线的值<0
        :param dist:
        :return:
        """
        for i in range(len(dist)):
            if dist[i][i] < 0:
                return True
        return False
        pass

    pass


if __name__ == "__main__":
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")

    v1.edges = [Edge(v3, -2)]
    v2.edges = [Edge(v1, 4), Edge(v3, 3)]
    v3.edges = [Edge(v4, 2)]
    v4.edges = [Edge(v2, -1)]

    graph = [v1, v2, v3, v4]

    FloydWarshall(graph).floyd_warshall()

    pass
