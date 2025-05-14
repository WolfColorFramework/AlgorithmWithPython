"""双向链表"""


class DoubleLinkedList:

    def __init__(self):
        self.head = DoubleLinkedList.DoubleNode(None, "head", None)
        self.tail = DoubleLinkedList.DoubleNode(None, "tail", None)
        self.head.next = self.tail
        self.tail.prev = self.head
        pass

    def insert(self, index, value):

        """
        插入
        :param index: 从0开始
        :param value:
        :return:
        """

        find_node = self._find_location(index - 1)
        if find_node is None:
            print(f"没有找到{index}位置")
        else:
            next_node = find_node.next
            new_node = self.DoubleNode(None, value, None)

            new_node.prev = find_node
            new_node.next = next_node

            find_node.next = new_node
            next_node.pre = new_node
        pass

    def remove(self, index):
        """
        删除
        :param index: 从0开始
        :return:
        """

        del_node = self._find_location(index)
        if del_node is None:
            raise IndexError(f"{index}超出界限范围")
        elif del_node is self.head or del_node is self.tail:
            raise IndexError(f"{index}为head/tail，不可删除")
        else:
            pre_node = del_node.prev
            next_node = del_node.next

            pre_node.next = next_node
            next_node.pre = pre_node
        pass

    def _find_location(self, index):

        result_index = -1

        node = self.head
        while node:
            if result_index == index:
                return node
            else:
                node = node.next
                result_index += 1
            pass
        pass

    def loop_print(self):

        node = self.head.next
        while node and node != self.tail:
            print(f"value:{node.value}")
            node = node.next
            pass
        print("None")
        pass

    # 节点
    class DoubleNode:
        def __init__(self, prev_node, value, next_node):
            self.prev = prev_node
            self.value = value
            self.next = next_node
            pass

        pass

    pass


if __name__ == "__main__":
    double_linked_list = DoubleLinkedList()
    double_linked_list.insert(0, 0)
    double_linked_list.insert(1, 1)
    double_linked_list.insert(2, 2)
    double_linked_list.insert(3, 3)

    double_linked_list.remove(10)

    double_linked_list.loop_print()
    pass
