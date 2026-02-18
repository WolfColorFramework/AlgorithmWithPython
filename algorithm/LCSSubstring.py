"""
最长公共字串
"""


class LCSSubstring:
    def __init__(self):
        pass

    def lcs(self, word1, word2):
        """
        :param word1: 字符串1
        :param word2: 字符串2
        :return: 公共字串长度
        """

        # 行:word2；列:word1
        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]

        for row_index, row_char in enumerate(word2):
            for col_index, col_char in enumerate(word1):
                if row_char == col_char:
                    if row_index == 0 or col_index == 0:
                        dp[row_index][col_index] = 1
                    dp[row_index][col_index] = dp[row_index - 1][col_index - 1] + 1
                else:
                    dp[row_index][col_index] = 0

        for row in dp:
            print(row)

        pass


if __name__ == "__main__":
    lcs = LCSSubstring()
    print(lcs.lcs("itheima", "thema"))

    pass
