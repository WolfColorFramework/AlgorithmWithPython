"""哈希表"""


class HashTable:

    def __init__(self):
        self.table = list()
        self.size = 0
        self.load_factor = 0.75
        self.threshold = len(self.table) * self.load_factor

    def get(self, key):
        index = hash(key) & (len(self.table) - 1)

        if self.table[index] is None:
            return None

        p = self.table[index]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None
        pass

    def put(self, key, value):
        index = hash(key) & (len(self.table) - 1)
        if self.table[index] is None:
            node = HashTable.Entry(key, value)
            self.table[index] = node
        else:
            node = self.table[index]
            while True:
                if node.key == key:
                    node.value = value
                    return
                if node.next is None:
                    break
                pass
            node.next = HashTable.Entry(key, value)
        self.size += 1

        if self.size > self.threshold:
            self.__resize()
            pass
        pass

    def __resize(self):
        """
        扩容
        :return:
        """
        new_table = (len(self.table) << 1) * None
        for index, p in enumerate(self.table):
            if p is not None:
                a = None
                b = None
                a_head = None
                b_head = None
                while p is not None:
                    if p.hash & len(self.table) == 0:
                        if a is not None:
                            a.next = p
                        pass
                    else:
                        if b is not None:
                            b.next = p
                        pass
                    p = p.next
                    if a is not None:
                        a.next = None
                        new_table[index] = a_head
                    else:
                        a_head = p
                        new_table[index + len(self.table)] = b_head
                    if b is not None:
                        b.next = None
                    else:
                        b_head = p
                pass
        self.table = new_table
        self.threshold = len(self.table) * self.load_factor
        pass

    def remove(self, key):
        index = hash(key) & (len(self.table) - 1)
        if self.table[index] is None:
            return None

        p = self.table[index]
        prev = None
        while p is not None:
            if p.key == key:
                if prev is None:
                    self.table[index] = p.next
                else:
                    prev.next = p.next
                self.size -= 1
                return p.value
            prev = p
            p = p.next
        pass

    class Entry:
        def __init__(self, key, value):
            self.hash = hash(key)
            self.key = key
            self.value = value
            self.next = None
            pass

    pass
