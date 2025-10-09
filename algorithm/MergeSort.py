"""
归并排序
"""


class MergeSort:

    def __init__(self, arr):
        self.array = arr
        pass

    def sort(self):
        arr2 = [None] * len(self.array)
        self.__split(self.array, 0, len(self.array) - 1, arr2)

    def print_sort(self):
        print(self.array)

    def __split(self, arr, left, right, arr2):
        """
        切分数组，排序，合并
        :param arr: 待排序数组
        :param left: 左边界
        :param right: 有边界
        :param arr2: 临时数组，收集排序后结果
        :return:
        """

        if left == right:
            return

        # 切分
        m = (left + right) >> 1
        self.__split(arr, left, m, arr2)
        self.__split(arr, m + 1, right, arr2)

        # 合并排序
        self.__merge(arr, left, m, m + 1, right, arr2)
        pass

    def __merge(self, arr, left, left_end, right, right_end, arr2):
        # 正确的索引处理
        i, j, k = left, right, left

        # 合并两个已排序的部分
        while i <= left_end and j <= right_end:
            if arr[i] < arr[j]:
                arr2[k] = arr[i]
                i += 1
            else:
                arr2[k] = arr[j]
                j += 1
            k += 1

        # 左数组已经无数据，右数组全部保存
        if i > left_end:
            arr2[k:k + (right_end - j + 1)] = arr[j:right_end + 1]

        # 右数组已经无数据，左数组全部保存
        if j > right_end:
            arr2[k:k + (left_end - i + 1)] = arr[i:left_end + 1]

        # 关键：将排序后的元素复制回原数组
        for i in range(left, right_end + 1):
            arr[i] = arr2[i]

    pass


if __name__ == "__main__":
    array = [1, 5, 6, 2, -1, 10, 11]
    merge_sort = MergeSort(array)
    merge_sort.sort()
    merge_sort.print_sort()
    pass
