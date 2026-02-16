"""
背包问题，无限数据
"""


class KnapsackProblemComplete:
    def __init__(self):
        self.items = [
            KnapsackProblemComplete.PackageItem(1, "青铜", 2, 3),
            KnapsackProblemComplete.PackageItem(2, "白银", 3, 4),
            KnapsackProblemComplete.PackageItem(3, "黄金", 4, 7),
        ]
        pass

    def select(self, total_weight):
        m, n = len(self.items), total_weight + 1  # m行n列
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 第一行数据处理
        for j in range(n):
            item0 = self.items[0]
            if j >= item0.weight:
                dp[0][j] = dp[0][j - item0.weight] + item0.value

        # 后续行数据处理
        for i in range(1, m):
            for j in range(n):
                item = self.items[i]
                if j >= item.weight: # 放的下
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - item.weight] + item.value)
                else:                # 放不下
                    dp[i][j] = dp[i - 1][j]

        return dp[m - 1][n - 1]
        pass

    class PackageItem:
        def __init__(self, index, name, weight, value):
            self.index = index
            self.name = name
            self.weight = weight
            self.value = value
            pass

        def __repr__(self):
            return f"{self.index}-{self.name}-{self.weight}-{self.value}"

        pass


if __name__ == "__main__":
    package1 = KnapsackProblemComplete()
    print(package1.select(6))

    pass
