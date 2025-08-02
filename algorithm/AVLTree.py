"""
avl搜索二叉树
"""


class AVLTree:

    def __init__(self):
        pass

    def height(self, tree_node):
        """
        树的高度
        :param tree_node:
        :return:
        """
        return 0 if tree_node is None else tree_node.height
        pass

    def max_depth(self, tree_node):
        """
        节点的最大深度
        :param tree_node:
        :return:
        """
        if tree_node is None:
            return 0

        left = self.max_depth(tree_node.left)
        right = self.max_depth(tree_node.right)
        return max(left, right) + 1
        pass

    def update_height(self, tree_node):
        """
        修改节点高度值
        :param tree_node:
        :return:
        """
        tree_node.height = max(self.height(tree_node.left), self.height(tree_node.right)) + 1
        pass

    def left_rotate(self, avl_node):
        """
        左旋
        :param avl_node: 要左旋的节点
        :return: 新的根节点
        """

        right_node = avl_node.right
        left_node = right_node.left
        right_node.left = avl_node
        avl_node.right = left_node

        # 更新节点高度
        self.update_height(avl_node)
        self.update_height(right_node)

        return right_node

        pass

    def right_rotate(self, avl_node):
        """
        右旋
        :param avl_node: 要右旋的节点
        :return: 新的根节点
        """

        left_node = avl_node.left
        right_node = left_node.right
        avl_node.left = right_node
        left_node.right = avl_node

        # 更新节点高度
        self.update_height(avl_node)
        self.update_height(left_node)

        return left_node
        pass

    def left_right_rotate(self, avl_node):
        """
        先左旋、再右旋
        :param avl_node:
        :return:
        """

        avl_node.left = self.left_rotate(avl_node.left)

        return self.right_rotate(avl_node)

        pass

    def right_left_rotate(self, avl_node):
        """
        先右旋、再左旋
        :param avl_node:
        :return:
        """

        avl_node.right = self.right_rotate(avl_node.right)

        return self.left_rotate(avl_node)

        pass

    def balance(self, avl_node):
        """
        平衡节点
        :param avl_node: 传入的节点
        :return:
        """

        if avl_node is None:
            return None

        bf = self.__balance_factor(avl_node)

        if bf > 1 and self.__balance_factor(avl_node) >= 0:
            # 左左
            return self.right_rotate(avl_node)
            pass
        elif bf > 1 and self.__balance_factor(avl_node) < 0:
            # 左右
            return self.left_right_rotate(avl_node)
            pass
        elif bf < -1 and self.__balance_factor(avl_node) > 0:
            # 右左
            return self.right_left_rotate(avl_node)
            pass
        elif bf < -1 and self.__balance_factor(avl_node) <= 0:
            # 右右
            return self.left_rotate(avl_node)
            pass

        return avl_node

        pass

    def __balance_factor(self, tree_node):
        """
        平衡因子
        :param tree_node:
        :return:
        """

        return self.height(tree_node.left) - self.height(tree_node.right)
        pass

    def put(self, avl_node, value):
        avl_node = self.__do_put(avl_node, value)
        pass

    def __do_put(self, avl_node, value):
        """
        递归插入
        :param avl_node: 当前节点
        :param value: 要插入的值
        :return:
        """

        if avl_node is None:
            return AVLTree.AVLNode(value, None, None, 1)

        if avl_node.value == value:
            avl_node.value = value
            return avl_node

        if avl_node.value > value:
            avl_node.left = self.__do_put(avl_node.left, value)
        else:
            avl_node.right = self.__do_put(avl_node.right, value)

        self.update_height(avl_node)
        return self.balance(avl_node)
        pass

    def remove(self, avl_node, key):
        avl_node = self.__do_remove(avl_node, key)
        pass

    def __do_remove(self, avl_node, key):
        """
        删除value的node
        :param avl_node: 树的root
        :param key:
        :return: 删除后剩余的节点
        """

        if avl_node is None:
            return None

        if key > avl_node.value:
            avl_node.right = self.__do_remove(avl_node.right, key)
            pass
        elif key < avl_node.value:
            avl_node.left = self.__do_remove(avl_node.left, key)
            pass
        else:
            if avl_node.left is None and avl_node.right is None:
                return avl_node
            elif avl_node.left is None:
                avl_node = avl_node.right
                pass
            elif avl_node.right is None:
                avl_node = avl_node.left
                pass
            else:
                s = avl_node.right
                while s.left is not None:
                    s = s.left
                    pass
                s.right = self.__do_remove(avl_node.right, s.value)
                s.left = avl_node.left
                avl_node = s
                pass
            pass

        self.update_height(avl_node)
        self.balance(avl_node)

        pass

    class AVLNode:
        def __init__(self, value, left, right, height):
            self.value = value
            self.left = left
            self.right = right
            self.height = height
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
