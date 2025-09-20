"""
avl搜索二叉树
"""


class BTree:

    def __init__(self, t):
        self.t = t  # 最小度数
        self.root = BTree.BNode(self.t)
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

    def split(self, left, parent, index):
        """
        节点分裂
        :param left:    待分裂节点
        :param parent:  待分裂节点的父节点
        :param index:   待分裂节点是在parent中的索引
        :return:
        """
        if parent is None:
            root = BTree.BNode(self.t)
            root.is_leaf = False
            root.insert_child(0, left)
            self.root = root
            parent = root
            pass

        right = BTree.BNode(self.t)
        right.is_leaf = left.is_leaf
        right.keys = left.keys[left.t:self.t + (self.t - 1)]
        if not left.is_leaf:
            right.children = left.children[self.t:self.t + self.t]
            pass

        # 中间的key（t-1）插入到父节点
        mid = left.keys[self.t - 1]
        parent.insert_key(index, mid)

        # right节点作为parent的节点
        parent.insert_child(index + 1, right)

        pass

    def __do_put(self, node, key, parent, index):
        i = 0
        while i < len(node.keys):
            if node.keys[i] == key:
                return  # 更新
            elif node.key[i] > key:
                break  # 找到位置
            i += 1
            pass

        if node.is_leaf:
            node.insert_key(i, key)
        else:
            self.__do_put(node.children[i], key, node, i)
        if len(node.keys) == self.max_key_num:
            self.split(node, parent, index)
        pass

    def remove(self, key):
        self.__do_remove(None, self.root, 0, key)
        pass

    def __do_remove(self, parent, node, index, key):
        i = 0
        while i < len(node.keys):
            if node.keys[i] >= key:
                break
            i += 1
        if node.is_leaf:
            if not self.find_node(i, key, node):
                return
                pass
            else:
                node.remove_key(i)
                pass
            pass
        else:
            if not self.find_node(i, key, node):
                self.__do_remove(node, node.children[i], i, key)
                pass
            else:
                s = node.children[i + 1]
                while not s.is_leaf:
                    s = s.children[0]
                s_key = s.keys[0]

                node.keys[i] = s_key

                self.__do_remove(node, node.children[i + 1], i + 1, s_key)
                pass

            pass
        if len(node.keys) < self.min_key_num:
            # 调整平衡
            self.balance(parent, node, index)
            pass
        pass

    def find_node(self, i, key, node):
        return i < len(node.keys) and node.keys[i] == key

    def balance(self, parent, node, index):
        if node is self.root:
            if len(self.root.keys) == 0 and self.root.children[0] is not None:
                self.root = self.root.children[0]

            return

        left = parent.child_left_sibling(index)
        right = parent.child_right_sibling(index)

        if left is not None and len(left.keys) > self.min_key_num:
            # 右旋
            node.insert_key(parent.keys[index - 1], 0)
            if not left.is_leaf:
                node.insert_chilid(0, left.remove_right_most_key())

            parent.keys.insert(index - 1, left.remove_left_most_key())
            return

        if right is not None and len(right.keys) > self.min_key_num:
            # 左旋
            node.insert_key(parent.keys[index], len(node.keys))
            if not node.is_leaf:
                node.insert_chilid(right.remove_left_most_child(), len(node.keys) + 1)
            parent.keys.insert(index, right.remove_left_most_key())
            return

        if left is not None:
            """
            向左兄弟合并
            """
            parent.children.pop(index)
            left.children.insert(len(left.keys), parent.keys.pop(index - 1))
            node.move_to_target(left)
            pass
        else:
            """
            向自己合并
            """
            parent.children.pop(index + 1)
            node.insert_key(parent.keys.pop(index), len(node.keys))
            right.move_to_target(node)
            pass

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

        def remove_key(self, index):
            t = self.keys[index]
            self.keys.pop(index)
            return t

        def remove_left_most_key(self):
            return self.remove_key(0)

        def remove_right_most_key(self):
            return self.remove_key(len(self.keys) - 1)

        def child_left_sibling(self, index):
            return self.children[index - 1] if index > 0 else None

        def child_right_sibling(self, index):
            return None if index == len(self.keys) else self.children[index + 1]

        def move_to_target(self, target):
            start = len(target.keys)
            if not self.is_leaf:
                for index, value in enumerate(target.keys):
                    target.children.insert(start + index, self.children[index])

            for index, value in enumerate(target.keys):
                target.keys.insert(len(target.keys), self.keys[index])

    pass


if __name__ == "__main__":
    # tree = BinaryTree()
    # tree.prev(tree.root)
    # tree.prev_while(tree.root)

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums_2 = nums[0:3]
    print(f"{nums_2}")

    pass
