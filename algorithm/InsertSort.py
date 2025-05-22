"""插入排序"""


class InsertSort:

    def __init__(self, disorder_array):
        self.array = disorder_array
        pass

    def insert_sort(self, low_index):
        """
        数组左边有序，右边无序，将右边无序的数据，插入到左边有序的序列
        :param low_index: 无序数组的起始位置（index）
        :return:
        """

        if low_index == len(self.array):
            return
            pass

        current_value = self.array[low_index]
        sort_index = low_index - 1  # 有序索引的高位
        while sort_index >= 0 and self.array[sort_index] > current_value:
            self.array[sort_index + 1] = self.array[sort_index]
            sort_index -= 1
            pass

        if sort_index + 1 != low_index:
            self.array[sort_index + 1] = current_value
            pass

        self.insert_sort(low_index + 1)
        pass

    def print_array(self):
        for num in self.array:
            print(f"{num}")
            pass
        pass

    pass


if __name__ == "__main__":
    array = [1, 2, 5, 3, 4, -1, 7]

    insert_sort = InsertSort(array)
    insert_sort.insert_sort(1)

    insert_sort.print_array()

    pass
