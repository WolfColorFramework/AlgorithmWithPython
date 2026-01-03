"""
拓扑排序
"""
from algorithm.Edge import Edge
from algorithm.Vertex import Vertex


class TopologicalSort:

    def topological_sort(self, graph):
        # 计算所有顶点得入度（这样才能找到入度为0的初始节点）
        for vertex in graph:
            for edge in vertex.edges:
                edge.linked.in_degree += 1

        vertex_queue = []
        for vertex in graph:
            if vertex.in_degree == 0:
                vertex_queue.append(vertex)

        # end

        while len(vertex_queue) > 0:
            vertex = vertex_queue.pop(0)
            print(f"{vertex.name}")
            for edge in vertex.edges:
                edge.linked.in_degree -= 1
                if edge.linked.in_degree == 0:
                    vertex_queue.append(edge.linked)
        pass

    def topological_sort2(self, graph):
        stack = []
        for vertex in graph:
            self.__dfs(vertex, stack)

        for result in stack[::-1]:
            print(f"{result.name}")

        pass

    def __dfs(self, vertex, stack):
        """
        深度优先
        :param vertex:
        :param stack:
        :return:
        """

        if vertex.visited:
            return

        for edge in vertex.edges:
            self.__dfs(edge.linked, stack)

        vertex.visited = True
        stack.append(vertex)

        pass

    pass


if __name__ == "__main__":
    v1 = Vertex("网页基础")
    v2 = Vertex("java基础")
    v3 = Vertex("javaWeb")
    v4 = Vertex("spring框架")
    v5 = Vertex("微服务框架")
    v6 = Vertex("数据库")
    v7 = Vertex("实战项目")

    v1.edges = [Edge(v3)]
    v2.edges = [Edge(v3)]
    v3.edges = [Edge(v4)]
    v6.edges = [Edge(v4)]
    v4.edges = [Edge(v5)]
    v5.edges = [Edge(v7)]
    v7.edges = []

    graph = [v1, v2, v3, v4, v5, v6, v7]

    topological_sort = TopologicalSort()
    # topological_sort.topological_sort(graph)

    topological_sort.topological_sort2(graph)

    pass
