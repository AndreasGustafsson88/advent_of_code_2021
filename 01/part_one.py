######################
# December 1st, Part 1
######################

from functools import reduce
from utils.helper_functions import time_ns

RAW_INPUT = 'input.txt'


def read_input(name: str) -> list[int]:
    """Reads input and converts to int"""

    with open(name, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


@time_ns
def count_depth_increase(sonar_sweep: list[int]) -> int:
    """Return length of list that only accepts numbers that are higher than previous"""

    return len([a for i, a in enumerate(sonar_sweep) if a > sonar_sweep[i - 1]])


@time_ns
def count_reduce(sonar_sweep: list[int]) -> dict:
    """Just playing around with a reduce solution"""

    return reduce(lambda a, b: a | {'inc': a['inc'] + 1, 'prev_nr': b} if b > a['prev_nr'] else a | {'prev_nr': b},
                  sonar_sweep, {'inc': 0, 'prev_nr': sonar_sweep[0] + 1})


if __name__ == '__main__':
    print(' Part One '.center(30, '*'))

    answer = count_depth_increase(read_input(RAW_INPUT))
    print(count_reduce(read_input(RAW_INPUT)))
    print(f'There are a total of {answer} depth increases that the sonar finds.')
