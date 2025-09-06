"""
avl搜索二叉树
"""


class AVLTree:

    def __init__(self, t):
        self.t = t  # 最小度数
        self.root = AVLTree.BNode(self.t)
        self.min_key_num = t - 1  # 最小key数目
        self.max_key_num = 2 * t - 1  # 最大key数目
        pass

    def contains(self, key):
        """
        是否包含key
        :param key:
        :return:
        """

        return self.root.get(key) != None

        pass

    def __do_put(self, node, key):
        i = 0
        while i < len(node.keys):
            if node.keys[i] == key:
                return  # 更新
            elif node.key[i] > key:
                break   # 找到位置
            i += 1
            pass

        if node.is_leaf:
            node.insert_key(i, key)
        else:
            self.__do_put(node.children[i], key)
        pass

    class BNode:
        def __init__(self, t):
            self.keys = list()  # 关键字数量2*t-1
            self.children = list()  # 孩子数量 2*t
            self.is_leaf = True  # 是否是叶子几点
            self.t = t  # 最小孩子数
            pass

        def get(self, key):
            i = 0
            while i < len(self.children):
                if self.keys[i] == key:
                    return self
                if self.keys[i] > key:
                    break
                i += 1
                pass

            if self.is_leaf:
                return None

            return self.children[i].get(key)
            pass

        def insert_key(self, index, key):

            i = len(self.children) - 1
            while i >= index:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[index] = key
            pass

        def insert_child(self, index, child):
            i = len(self.children) - 1
            while i >= index:
                self.children[i + 1] = self.children[i]
                i -= 1
            self.children[index] = child
            pass

    pass


if __name__ == "__main__":
    # tree = BinaryTree()
    # tree.prev(tree.root)
    # tree.prev_while(tree.root)

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums_2 = nums[0:3]
    print(f"{nums_2}")

    pass
