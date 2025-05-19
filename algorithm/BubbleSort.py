"""冒泡排序"""


class BubbleSort:

    def __init__(self, disorder_array):
        self.array = disorder_array
        pass

    def bubble_sort(self):
        length = len(self.array)

        for num in self.array:
            index = 0
            while index < length - 1:  # 冒泡排序内层循环，默认第一个数是有序的，所以index<length-1
                if self.array[index] > self.array[index + 1]:
                    tmp = array[index + 1]
                    self.array[index + 1] = self.array[index]
                    self.array[index] = tmp
                    pass
                index += 1
                pass
            pass
        pass

    # 递归调用
    def bubble_sort_2(self, high_index):

        if high_index == 0:
            return
            pass

        index = 0
        while index < high_index:
            if self.array[index] > self.array[index + 1]:
                tmp = array[index + 1]
                self.array[index + 1] = self.array[index]
                self.array[index] = tmp
                pass
            index += 1
            pass

        self.bubble_sort_2(high_index - 1)
        pass

    def print_array(self):
        for num in self.array:
            print(f"{num}")
            pass
        pass

    pass


if __name__ == "__main__":
    array = [4, 1, 8, 9, 5, 3]

    bubble_sort = BubbleSort(array)
    # bubble_sort.bubble_sort()

    bubble_sort.bubble_sort_2(len(bubble_sort.array) - 1)

    bubble_sort.print_array()

    pass
