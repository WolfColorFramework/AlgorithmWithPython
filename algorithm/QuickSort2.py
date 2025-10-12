"""
快速排序2
"""


class QuickSort2:
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

        pv = arr[left]  # 基准点
        i, j = left, right  # i找大的 j找小的
        while i < j:
            # j找小的
            while i < j and arr[j] > pv:
                j -= 1

            # i找大的
            while i < j and arr[i] <= pv:
                i += 1

            # 交换位置
            self.__swap(arr, i, j)

            pass

        self.__swap(arr, left, i)
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
    shell_sort = QuickSort2(array)
    shell_sort.sort()
    shell_sort.print_sort()
    pass
