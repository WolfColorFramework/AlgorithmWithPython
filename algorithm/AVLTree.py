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

    def balance_factor(self, tree_node):
        """
        平衡因子
        :param tree_node:
        :return:
        """

        return self.height(tree_node.left) - self.height(tree_node.right)
        pass

    def prev(self, tree_node):
        """前序遍历 中左右"""

        if tree_node is None:
            return
            pass

        print(f"{tree_node.value} ", end="")

        self.prev(tree_node.left)
        self.prev(tree_node.right)

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
