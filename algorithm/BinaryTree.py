"""二叉树遍历"""

from collections import deque


class BinaryTree:

    def __init__(self):
        d = BinaryTree.TreeNode("d", None, None)
        e = BinaryTree.TreeNode("e", None, None)
        f = BinaryTree.TreeNode("f", None, None)
        b = BinaryTree.TreeNode("b", d, e)
        c = BinaryTree.TreeNode("c", f, None)
        self.root = BinaryTree.TreeNode("a", b, c)

        self.stack = deque()
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

    def prev_while(self, tree_node):
        node = tree_node
        curr_node = node
        while node is not None or len(self.stack) != 0:
            if node is not None:
                print(f"{node.value} ", end="")
                self.stack.append(node)
                curr_node = node
                node = node.left
            else:
                pop = self.stack.pop()
                if curr_node != node:
                    node = pop.right
            pass
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

        def __eq__(self, other):
            if not isinstance(other, BinaryTree.TreeNode):
                return False
            return self.value == other.value  # 按属性值比较

        pass

    pass


if __name__ == "__main__":
    tree = BinaryTree()
    tree.prev(tree.root)
    tree.prev_while(tree.root)

    pass
