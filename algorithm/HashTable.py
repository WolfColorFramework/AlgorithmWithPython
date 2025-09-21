"""哈希表"""


class HashTable:

    def __init__(self):
        self.table = list()
        self.size = 0

    def get(self, hash, key):
        index = hash & (len(self.table) - 1)

        if self.table[index] is None:
            return None

        p = self.table[index]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None
        pass

    def put(self, hash, key, value):
        index = hash & (len(self.table) - 1)
        if self.table[index] is None:
            node = HashTable.Entry(hash, key, value)
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
            node.next = HashTable.Entry(hash, key, value)
        self.size += 1
        pass

    def remove(self, hash, key):
        pass

    class Entry:
        def __init__(self, hash, key, value):
            self.hash = hash
            self.key = key
            self.value = value
            self.next = None
            pass

    pass
