"""汉诺塔"""


class HanoiTower:
    def __init__(self):
        pass

    def move(self, num, tower1, tower2, tower3):
        """
        将最大的数移动到塔3，然后将塔2的都移动到塔3
        :param num:
        :param tower1: 塔1
        :param tower2: 塔2
        :param tower3: 塔3
        :return:
        """
        if num == 0:
            return
            pass

        self.move(num - 1, tower1, tower3, tower2)

        # a-》c
        last = tower1.pop()
        tower3.append(last)

        self.print_tower(tower1, tower2, tower3)

        self.move(num - 1, tower2, tower1, tower3)
        pass

    pass

    def print_tower(self, tower1, tower2, tower3):
        print(f"tower1:{tower1}")
        print(f"tower2:{tower2}")
        print(f"tower3:{tower3}")

        pass


if __name__ == "__main__":
    list_a = list(range(3, 0, -1))
    list_b = list()
    list_c = list()

    # list_a.pop()

    tower = HanoiTower()
    tower.move(3, list_a, list_b, list_c)

    print(f"{list_c}")

    pass
