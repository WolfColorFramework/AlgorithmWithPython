"""优先队列"""


class PriorityQueue:

    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0
        pass

    def offer(self, num):
        """
        插入新元素
        :param num: 待插入数据
        :return:
        """

        if self.is_full():
            return False
            pass

        # 插入末尾
        last_index = self.size
        self.array[last_index] = num

        # 开始上浮，形成大顶堆
        self._up(last_index)

        self.size += 1
        return True

        pass

    def _up(self, index):
        value = self.array[index]
        parent_index = (index - 1) >> 1
        while index > 0 and value > self.array[parent_index]:
            self.array[index] = self.array[parent_index]
            index = parent_index
            parent_index = (index - 1) >> 1
            pass
        self.array[index] = value
        pass

    def poll(self):
        """
        删除堆顶元素
        :return: 删除的元素
        """

        if self.size == 0:
            return None

        top = self.array[0]
        self.array[0] = self.array[self.size - 1]

        self._down(0)

        # 容量-1
        self.size -= 1

        return top

        pass

    def _down(self, index):

        if index > self.size - 1:
            return

        left_index = 2 * index + 1
        right_index = left_index + 1

        if left_index > self.size - 1 or right_index > self.size - 1:
            return

        max_index = index
        if self.array[left_index] > self.array[max_index]:
            max_index = left_index
            pass
        if self.array[right_index] > self.array[max_index]:
            max_index = right_index
            pass

        if max_index != index:
            temp = self.array[index]
            self.array[index] = self.array[max_index]
            self.array[max_index] = temp

            self._down(max_index)
            pass
        pass

    def peek(self):
        """
        获取堆顶元素
        :return:
        """

        return self.array[0]

        pass

    def is_full(self):
        """
        堆是否满
        :return:
        """

        return self.size == len(self.array)

        pass

    def print(self):
        for index, number in enumerate(self.array):
            print(f"index:{index},value:{number}")
        print("None")

    pass


if __name__ == "__main__":
    priorityQueue = PriorityQueue(5)
    priorityQueue.offer(4)
    priorityQueue.offer(3)
    priorityQueue.offer(2)
    priorityQueue.offer(5)
    priorityQueue.offer(1)
    # priorityQueue.print()

    print("=====================")

    # num = priorityQueue.poll()
    #
    # print(f"{num}，{priorityQueue.size}")

    while priorityQueue.size > 0:
        num = priorityQueue.poll()
        print(f"{num}，{priorityQueue.size}")

        pass
pass
