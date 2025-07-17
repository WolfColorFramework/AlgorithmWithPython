"""二叉树遍历"""


class BinaryTree:

    def __init__(self):
        d = BinaryTree.TreeNode("d", None, None)
        e = BinaryTree.TreeNode("e", None, None)
        f = BinaryTree.TreeNode("f", None, None)
        b = BinaryTree.TreeNode("b", d, e)
        c = BinaryTree.TreeNode("c", f, None)
        self.root = BinaryTree.TreeNode("a", b, c)
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

    def middle(self, tree_node):
        """中序遍历 左中右"""
        if tree_node is None:
            return
            pass

        self.middle(tree_node.left)
        print(f"{tree_node.value} ", end="")
        self.middle(tree_node.right)

        pass

    def post(self, tree_node):
        """后续遍历 左右中"""
        if tree_node is None:
            return
            pass

        self.post(tree_node.left)
        self.post(tree_node.right)
        print(f"{tree_node.value} ", end="")

        pass

    class TreeNode:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right
            pass

        pass

    pass


if __name__ == "__main__":
    tree = BinaryTree()
    tree.prev(tree.root)

    pass
