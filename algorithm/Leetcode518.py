"""

"""


class Leetcode518:
    def __init__(self):
        self.coins = [5, 2, 1]
        pass

    def rec(self, coin_amount, coins, amount, stack, first):
        """
        :param coin_amount: 硬币面值
        :param coins: 硬币面值数组
        :param amount: 剩余金额
        :param stack: 记录组装结果
        :param first: 是否第一次调用
        :return: 满足结果的个数
        """

        if first is not True:
            stack.append(coin_amount)
            pass
        if amount < 0:
            if len(stack) > 0:
                stack.pop()
            return 0
        elif amount == 0:
            print(f"有解:{stack}")
            if len(stack) > 0:
                stack.pop()
            return 1
        else:
            result = 0
            for coin in coins:
                if coin_amount <= coin:
                    result += self.rec(coin, coins, amount - coin, stack, False)
                    pass
                pass

            if len(stack) > 0:
                stack.pop()

            return result
        pass


if __name__ == "__main__":
    result = Leetcode518().rec(1, Leetcode518().coins, 5, list(), True)

    print(f"{result}")

    pass
