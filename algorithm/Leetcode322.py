"""

"""


class Leetcode322:
    def __init__(self):
        pass

    def rec(self, coins, amount):
        """
        :param coins: 硬币面值数组
        :param amount: 需要组合成的金额总数
        :return: 满足结果的个数
        """

        reminder = amount  # 剩余金额
        count = 0  # 金币数量
        for coin in coins:
            while reminder > coin:
                reminder -= coin
                count += 1
                pass
            if reminder == coin:
                reminder -= coin
                count += 1
                break
                pass

        if reminder == 0:
            return count
        else:
            return -1

        pass


if __name__ == "__main__":
    result = Leetcode322().rec([5, 2, 1], 18)

    print(f"{result}")

    pass
