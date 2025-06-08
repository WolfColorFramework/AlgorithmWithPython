"""链表删除中的所有指定元素"""


class LinkedDel:
    def __init__(self, node):
        self.head = node
        pass

    def del_node(self, node, del_value):
        if node is None:
            return
            pass

        if node.value == del_value:
            return self.del_node(node.next, del_value)
            pass
        else:
            node.next = self.del_node(node.next, del_value)
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
    node7 = LinkedDel.ListNode(7, None)
    node6 = LinkedDel.ListNode(6, node7)
    node5 = LinkedDel.ListNode(5, node6)
    node4 = LinkedDel.ListNode(4, node5)
    node3 = LinkedDel.ListNode(6, node4)
    node2 = LinkedDel.ListNode(6, node3)
    node1 = LinkedDel.ListNode(1, node2)

    linkedDel = LinkedDel(node1)
    linkedDel.del_node(linkedDel.head, 6)
    linkedDel.print_linked()

    pass
