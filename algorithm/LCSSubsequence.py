"""
最长公共子序列
"""


class LCSSubsequence:
    def __init__(self):
        pass

    def lcs(self, word1, word2):
        """
        :param word1: 源字符串
        :param word2: 比较字符串
        :return: 最长公共子序列
        """

        # 行:word2；列:word1
        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]

        for row_index, row_char in enumerate(word2):
            for col_index, col_char in enumerate(word1):
                if row_char == col_char:    # 相同字符
                    if row_index == 0 or col_index == 0:
                        dp[row_index][col_index] = 1
                    dp[row_index][col_index] = dp[row_index - 1][col_index - 1] + 1
                else:   # 不同字符
                    dp[row_index][col_index] = max(dp[row_index - 1][col_index], dp[row_index][col_index - 1])

        for row in dp:
            print(row)

        return dp[-1][-1]

        pass


if __name__ == "__main__":
    lcs = LCSSubsequence()
    print(lcs.lcs("abcxyz", "abxyz"))
    pass
