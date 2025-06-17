"""合并2个有序链表"""


class MergeTwoLinked:
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

    class ListNode:
        def __init__(self, value, next):
            self.value = value
            self.next = next
            pass

        pass

    pass


if __name__ == "__main__":
    node_4 = MergeTwoLinked.ListNode(4,None)
    node_3 = MergeTwoLinked.ListNode(3,node_4)
    node_2 = MergeTwoLinked.ListNode(2, node_3)
    linked_1 = MergeTwoLinked.ListNode(1, node_2)

    node_5 = MergeTwoLinked.ListNode(9, None)
    linked_2 = MergeTwoLinked.ListNode(8, node_5)

    mergeTwo = MergeTwoLinked()
    merge_linked = mergeTwo.merge(linked_1, linked_2)
    mergeTwo.print_linked(merge_linked)

    pass
