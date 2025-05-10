from algorithm.BinarySearch import BinarySearch
from algorithm.SinglyLinkedList import SinglyLinkedList

# 二分法
binarySearch = BinarySearch()
array = [1, 2, 3, 4, 5, 6, 7]
array_left = [1, 2, 3, 3, 3, 6, 7]

# 二分查找-1
# result = binarySearch.binary_search_basic(array, 7)
# print(result)

# 二分查找-2
# result = binarySearch.binary_search_basic2(array, 100)
# print(result)

# 平衡查找
# result = binarySearch.binary_search_balance(array, 1)
# print(result)

# 最左侧查找法
# result = binarySearch.binary_search_left(array_left, 3)
# print(result)

# 最右侧查找法
# result = binarySearch.binary_search_right(array_left, 3)
# print(result)


# 单向链表
singlyLinked = SinglyLinkedList(None)
singlyLinked.add_head(1)
singlyLinked.add_head(2)
singlyLinked.add_head(3)
singlyLinked.loop_print()