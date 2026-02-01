"""
不相交集合
"""


class DisjointSet:
    def __init__(self, size):
        self.elements = list(range(size))
        for i in self.elements:
            self.elements[i] = i

    def find(self, x):
        if x == self.elements[x]:
            return x
        self.elements[x] = self.find(self.elements[x])
        return self.elements[x]

    def union(self, x, y):
        """
        x,y 集合中的老大索引
        :param x:
        :param y:
        :return:
        """
        self.elements[y] = x
