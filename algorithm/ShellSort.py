"""
希尔排序
"""


class ShellSort:
    def __init__(self, arr):
        self.array = arr
        pass

    def sort(self):
        gap = len(array) >> 1  # 相当于 array.length // 2
        while gap >= 1:
            for i in range(gap, len(self.array)):
                t = self.array[i]  # 待排序元素
                n = i - gap  # 已排序元素索引

                # 从右向左找插入位置，如果t>self.array[n],self.array[n]就要向右边移动，空出位置给t
                while n >= 0 and t < self.array[n]:
                    self.array[n + gap] = self.array[n]
                    n -= gap

                # 找到插入位置
                if n != i - gap:
                    self.array[n + gap] = t

            gap = gap >> 1  # 相当于 gap // 2

    def print_sort(self):
        print(self.array)

    pass


if __name__ == "__main__":
    array = [1, 5, 6, 2, -1, 10, 11]
    shell_sort = ShellSort(array)
    shell_sort.sort()
    shell_sort.print_sort()
    pass
