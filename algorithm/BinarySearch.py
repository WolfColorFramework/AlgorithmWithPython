"""二分查找"""


class BinarySearch:

    def binary_search_basic(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            m = int((right + left) >> 1)  # (right+left) / 2 这种/2的实现，在array非常大的时候会导致数据溢出，所以>>>1 更安全
            if target > array[m]:  # 待查找数据在右边
                left = m + 1
            elif target < array[m]:  # 待查找数据在左边
                right = m - 1
            else:
                return m
        return -1

    # 第二种实现，这种实现就是right表示边界，不代表要比较的元素
    def binary_search_basic2(self, array, target):
        left, right = 0, len(array)
        while left < right:
            m = int((right + left) >> 1)  # 中间点
            if target > array[m]:
                left = m + 1
            elif target < array[m]:
                right = m
            else:
                return m
        return -1

    # 平衡查找方法
    def binary_search_balance(self, array, target):
        left, right = 0, len(array)
        while left < right:
            m = int((right + left) >> 1)  # 中间点
            if target > array[m]:
                left = m + 1
            elif target < array[m]:
                right = m
            else:
                return m
        return -1

    # 查找最左侧索引
    def binary_search_left(self, array, target):
        left, right = 0, len(array) - 1
        resultIndex = -1
        while left <= right:
            m = int((right + left) >> 1)  # /2 操作
            if target > array[m]:  # 待查找数据在右边
                left = m + 1
            elif target < array[m]:  # 待查找数据在左边
                right = m - 1
            else:
                resultIndex = m
                right = m - 1
        return resultIndex

    # 查找最右侧索引
    def binary_search_right(self, array, target):
        left, right = 0, len(array) - 1
        result_index = -1
        while left <= right:
            m = int((right + left) >> 1)  # /2 操作
            if target > array[m]:  # 待查找数据在右边
                left = m + 1
            elif target < array[m]:  # 待查找数据在左边
                right = m - 1
            else:
                result_index = m
                left = m + 1
        return result_index

    pass


if __name__ == "__main__":
    a, b = 0, 7
    print((a + b) / 2)
    pass
