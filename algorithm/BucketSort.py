from algorithm.QuickSort import QuickSort

"""
桶排序
"""


class BucketSort:
    def __init__(self, arr):
        self.source_arr = arr
        self.bucket_arr = [list()] * 10
        for idx, value in enumerate(self.bucket_arr):
            self.bucket_arr[idx] = list()
        pass

    def sort(self):

        # 放入桶
        for value in self.source_arr:
            index = value // 10
            self.bucket_arr[index].append(value)

        # 排序桶内元素
        index = 0
        for bucket in self.bucket_arr:
            sort_handler = QuickSort(bucket)
            sort_handler.sort()

            for value in sort_handler.array:
                self.source_arr[index] = value
                index += 1

        pass

    def print_sort(self):
        print(self.source_arr)

    pass


if __name__ == "__main__":
    array = [20, 18, 28, 66, 25, 31, 67, 30]
    shell_sort = BucketSort(array)
    shell_sort.sort()
    shell_sort.print_sort()
    pass
