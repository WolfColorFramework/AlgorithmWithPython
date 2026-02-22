"""
卡特兰树
"""


class Catalan:
    def __init__(self):
        pass

    def catalan(self, n):
        dp = list([0] * (n + 1))
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):  # i:第i个卡特兰树
            for j in range(i):  # 拆分的循环
                print(f"({j},{i - 1 - j})", end="\t")
                dp[i] += dp[j] * dp[i - 1 - j]
            print("", end="\n")

        return dp[n]

        pass


if __name__ == "__main__":
    catalan = Catalan()
    result = catalan.catalan(5)
    print(result)
    pass
