"""
动态规划，解决凑总金额问题
"""


class Leetcode518_2:
    def __init__(self):
        self.coins = [1, 2, 5]
        pass

    def rec(self, amount):

        # 初始化二维数组
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(self.coins))]

        # 第一列初始化为1
        for row in dp:
            row[0] = 1

        # 第一个银币
        for i in range(1, amount + 1):
            if i >= self.coins[0]:
                dp[0][i] = dp[0][i - self.coins[0]]
                pass

        # 其余硬币，递推式
        for i in range(1, len(self.coins)):
            for j in range(1, amount + 1):
                if j >= self.coins[i]:  # 放得下
                    dp[i][j] = dp[i - 1][j] + dp[i][j - self.coins[i]]
                else:  # 放不下
                    dp[i][j] = dp[i - 1][j]

        print(f"{dp}")

        pass

    pass


if __name__ == "__main__":
    Leetcode518_2().rec(5)

pass
