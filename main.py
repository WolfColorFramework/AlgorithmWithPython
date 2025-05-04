from algorithm.BinarySearch import BinarySearch

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

# 最左侧
result = binarySearch.binary_search_left(array_left, 100)
print(result)