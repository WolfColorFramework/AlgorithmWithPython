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
