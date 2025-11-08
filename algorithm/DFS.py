"""
深度优先搜索
"""
from algorithm.Edge import Edge
from algorithm.Vertex import Vertex


class DFS:

    def dfs(self, vertex):
        vertex.visited = True
        print(f"{vertex.name}")

        for edge in vertex.edges:
            if not edge.linked.visited:
                self.dfs(edge.linked)
        pass

    def dfs2(self, vertex):
        stack = [vertex]
        while len(stack) > 0:
            pop = stack.pop()
            pop.visited = True
            print(f"{pop.name}")
            for edge in pop.edges:
                if not edge.linked.visited:
                    stack.append(edge.linked)
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

    v1.edges = [Edge(v3), Edge(v2), Edge(v6)]
    v2.edges = [Edge(v4)]
    v3.edges = [Edge(v4), Edge(v6)]
    v4.edges = [Edge(v5)]
    v5.edges = []
    v6.edges = [Edge(v5)]

    dfs = DFS()
    dfs.dfs(v1)

    pass
