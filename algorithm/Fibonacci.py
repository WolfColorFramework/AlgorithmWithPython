"""
斐波那契额数列
"""


class Fibonacci:
    def __init__(self):
        pass

    def get(self, i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            a, b = 0, 0
            for j in range(i):
                if j == 0:
                    a = 0
                    continue
                elif j == 1:
                    b = 1
                    continue
                else:
                    c = a + b
                    a = b
                    b = c
                pass
            return b


if __name__ == "__main__":
    fib = Fibonacci()
    print(fib.get(13))
    pass
