"""
快速排序
"""


class QuickSort:
    def __init__(self, arr):
        self.array = arr
        pass

    def sort(self):
        self.__quick(self.array, 0, len(self.array) - 1)
        pass

    def __quick(self, arr, left, right):
        if left >= right:
            return

        p = self.__partition(self.array, left, right)
        self.__quick(arr, left, p - 1)
        self.__quick(arr, p + 1, right)
        pass

    def __partition(self, arr, left, right):
        """
        分区方法
        :param arr:
        :param left:
        :param right:
        :return: 基准点索引
        """

        pv = arr[right]  # 基准点
        i, j = left, left  # i找大的 j找小的
        while j < right:
            if arr[j] < pv:  # j找到小的
                if i != j:
                    self.__swap(arr, i, j)
                i += 1  # i自增（i没找到大的）
            j += 1
            pass

        self.__swap(arr, i, right)
        return i
        pass

    def __swap(self, arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        pass

    def print_sort(self):
        print(self.array)

    pass


if __name__ == "__main__":
    array = [1, 5, 6, 2, -1, 10, 11]
    shell_sort = QuickSort(array)
    shell_sort.sort()
    shell_sort.print_sort()
    pass
