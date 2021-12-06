######################
# December 6th, Part 1
######################


class PoolOfLanternfish(dict):

    def __init__(self, fish):
        self.fish = [Fish(f) for f in fish]
        super().__init__()

    @property
    def population(self):
        return len(self.fish)

    def age_one_day(self):
        toddlers = list(filter(lambda x: x is not None, [f.age() for f in self.fish]))
        if toddlers:
            [self.fish.append(t) for t in toddlers]


class Fish:

    def __init__(self, cycle):
        self.cycle: int = cycle

    def reset_cycle(self):
        self.cycle = 6

    @staticmethod
    def give_birth():
        return Fish(8)

    def age(self):
        if self.cycle == 0:
            self.reset_cycle()
            return Fish.give_birth()
        else:
            self.cycle -= 1


def read_input(name: str) -> list:
    """Returns all values as a separate int in list"""
    with open(name, 'r') as f:
        return [int(line.strip()) for line in f.read().split(',')]


if __name__ == "__main__":
    NR_DAYS = 80
    RAW_INPUT = 'input.txt'

    fish = read_input(RAW_INPUT)
    school_of_lanternfish = PoolOfLanternfish(fish)

    for i in range(1, NR_DAYS + 1):
        school_of_lanternfish.age_one_day()

    print(' Part One '.center(30, '*'))
    print(f'The total size of the school of lanternfish after {NR_DAYS} is {school_of_lanternfish.population}')