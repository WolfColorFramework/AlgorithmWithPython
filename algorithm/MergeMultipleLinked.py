"""合并2个有序链表"""


class MergeMultipleLinked:
    def __init__(self):
        pass

    def merge(self, linked1, linked2):
        if linked1 is None:
            return linked2
            pass

        if linked2 is None:
            return linked1
            pass

        if linked1.value <= linked2.value:
            linked1.next = self.merge(linked1.next, linked2)
            return linked1
            pass
        else:
            linked2.next = self.merge(linked1, linked2.next)
            return linked2
            pass

        pass

    def print_linked(self, linked):

        while linked:
            print(f"value:{linked.value}")
            linked = linked.next
            pass
        print("None")
        pass

    def split(self, list_nodes, i, j):
        """
        合并后的链表
        :param list_nodes:
        :param i:
        :param j:
        :return:
        """

        if i == j:
            return list_nodes[i]
            pass

        middle = (i + j) >> 1
        left = self.split(list_nodes, i, middle)
        right = self.split(list_nodes, middle + 1, j)
        return self.merge(left, right)

        pass

    def merge_multiple(self, list_nodes):
        if len(list_nodes) == 0:
            return None
            pass

        return self.split(list_nodes, 0, len(list_nodes) - 1)

        pass

    class ListNode:
        def __init__(self, value, next):
            self.value = value
            self.next = next
            pass

        pass

    pass


if __name__ == "__main__":
    node_4 = MergeMultipleLinked.ListNode(4, None)
    node_3 = MergeMultipleLinked.ListNode(3, node_4)
    node_2 = MergeMultipleLinked.ListNode(2, node_3)
    linked_1 = MergeMultipleLinked.ListNode(1, node_2)

    node_5 = MergeMultipleLinked.ListNode(9, None)
    linked_2 = MergeMultipleLinked.ListNode(8, node_5)

    node_6 = MergeMultipleLinked.ListNode(6, None)
    linked_3 = MergeMultipleLinked.ListNode(5, node_6)

    node_7 = MergeMultipleLinked.ListNode(15, None)
    node_8 = MergeMultipleLinked.ListNode(13, node_7)
    node_9 = MergeMultipleLinked.ListNode(12, node_8)
    linked_4 = MergeMultipleLinked.ListNode(10, node_9)

    list_nodes = [linked_1, linked_2, linked_3, linked_4]

    merge_multiple = MergeMultipleLinked()
    merge_linked = merge_multiple.merge_multiple(list_nodes)
    merge_multiple.print_linked(merge_linked)

    pass
