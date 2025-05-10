"""单向链表"""


class SinglyLinkedList:

    def __init__(self, head):
        self.head = head
        pass

    def add_head(self, value):

        newNode = self.Node(value, None)
        newNode.next = self.head
        self.head = newNode

        pass

    def loop_print(self):

        node = self.head
        while node:
            print(f"value:{node.value}")
            node = node.next
            pass
        print("None")
        pass

    # 节点
    class Node:
        def __init__(self, value, next_node):
            self.value = value
            self.next = next_node
            pass
        pass

    pass