"""删除所有相同的元素"""


class DelAllSameNum:
    def __init__(self, node):
        self.head = node
        pass

    def del_node(self, node):
        if node is None or node.next is None:
            return node
            pass

        if node.value == node.next.value:
            dif_node = node.next.next
            while dif_node is not None and dif_node.value == node.value:
                dif_node = dif_node.next
                pass

            return self.del_node(dif_node)
            pass
        else:
            node.next = self.del_node(node.next)
            return node
            pass

        pass

    def print_linked(self):

        node = self.head
        while node:
            print(f"value:{node.value}")
            node = node.next
            pass
        print("None")
        pass

    class ListNode:
        def __init__(self, value, next):
            self.value = value
            self.next = next
            pass

        pass

    pass


if __name__ == "__main__":

    node7 = DelAllSameNum.ListNode(6, None)
    node6 = DelAllSameNum.ListNode(5, node7)
    node5 = DelAllSameNum.ListNode(4, node6)
    node4 = DelAllSameNum.ListNode(2, node5)
    node3 = DelAllSameNum.ListNode(2, node4)
    node2 = DelAllSameNum.ListNode(2, node3)
    node1 = DelAllSameNum.ListNode(1, node2)

    del_linked = DelAllSameNum(node1)
    del_linked.del_node(del_linked.head)
    del_linked.print_linked()

    pass
