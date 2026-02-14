"""
背包问题
"""


class KnapsackProblem:
    def __init__(self):
        self.items = [
            KnapsackProblem.PackageItem(0, 4, 24),
            KnapsackProblem.PackageItem(1, 8, 160),
            KnapsackProblem.PackageItem(2, 2, 4000),
            KnapsackProblem.PackageItem(3, 6, 108),
            KnapsackProblem.PackageItem(4, 1, 4000),
        ]
        pass

    def solve(self, total_weight):
        # 1. 倒叙
        self.items.sort(key=lambda x: x.unit_value, reverse=True)

        # 2. 贪心，每次取最大的
        max = 0
        for item in self.items:
            if total_weight >= item.weight:
                max += item.value
                total_weight -= item.weight
            else:
                max += item.unit_value * total_weight
                break

        print(max)
        pass


    class PackageItem:
        def __init__(self, index, weight, value):
            self.index = index
            self.weight = weight
            self.value = value
            self.unit_value = value / weight
            pass

        def __repr__(self):
            return f"{self.index} {self.weight} {self.value}"

        pass


if __name__ == "__main__":

    problem = KnapsackProblem()
    problem.solve(10)

    pass
