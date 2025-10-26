"""
计数排序
"""


class CountingSort:
    def __init__(self, arr):
        self.source_arr = arr
        self.count_arr = [0] * (max(self.source_arr) + 1)
        pass

    def sort(self):
        # 统计计数
        for value in self.source_arr:
            self.count_arr[value] += 1

        # 排序结果
        index = 0   # 存放元素索引
        for idx, value in enumerate(self.count_arr):
            while value > 0:
                self.source_arr[index] = idx
                value -= 1
                index += 1
            pass

        pass

    def print_sort(self):
        print(self.source_arr)

    pass


if __name__ == "__main__":
    array = [5, 1, 1, 3, 0]
    shell_sort = CountingSort(array)
    shell_sort.sort()
    shell_sort.print_sort()
    pass
