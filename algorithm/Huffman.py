"""
哈夫曼树
"""
from queue import PriorityQueue


class HuffmanTree:

    def __init__(self, str):
        self.str = str
        self.map = {}  # key:字符,value:节点
        self.pq = PriorityQueue()
        self.root = None

        # 1.计算频次
        for char in str:
            if char not in self.map:
                self.map[char] = HuffmanTree.TreeNode(char, 1, None, None, "")
            else:
                self.map[char].freq += 1

        print("打印频次")
        for k, v in self.map.items():
            print(f"key:{k},value:{v.freq}")

        # 添加元素
        for k, v in self.map.items():
            self.pq.put(v)

        # 2.构造树
        while self.pq.qsize() >= 2:
            x = self.pq.get()
            y = self.pq.get()
            freq = x.freq + y.freq
            self.root = HuffmanTree.TreeNode(None, freq, x, y, "")
            self.pq.put(self.root)

        # 计算编码
        self.__dfs(self.pq.get(), "")

        print("打印最终code")
        for k, v in self.map.items():
            print(f"key:{k},value:{v.code}")
        pass

    def __dfs(self, node, result):
        if node.is_leaf():
            print(f"{node.ch}:{result}")
            node.code = result
        else:
            self.__dfs(node.left, result + "0")
            self.__dfs(node.right, result + "1")

        if len(result) > 0:
            result = result[:-1]
        pass

    def encode(self):
        result = ""
        for char in self.str:
            result += self.map[char].code
        return result

    def decode(self, str):
        result = ""
        node = self.root
        for char in str:
            if char == "0":
                node = node.left
            elif char == "1":
                node = node.right
            if node.is_leaf():
                result += node.ch
                node = self.root
        return result

    class TreeNode:
        def __init__(self, ch, freq, left, right, code):
            self.ch = ch
            self.freq = freq
            self.left = left
            self.right = right
            self.code = code
            pass

        def __eq__(self, other):
            if not isinstance(other, HuffmanTree.TreeNode):
                return False
            return self.value == other.value  # 按属性值比较

        def __lt__(self, other):
            # 定义比较规则：优先级数字越小，优先级越高
            return self.freq < other.freq

        def is_leaf(self):
            return self.left is None and self.right is None

        pass

    pass


if __name__ == "__main__":
    HuffmanTree = HuffmanTree("abbccccccc")
    encod_str = HuffmanTree.encode()
    print(HuffmanTree.decode(encod_str))

    pass
