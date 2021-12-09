######################
# December 9th, Part 1
######################

import numpy as np


def read_input(name: str) -> np.array:
    with open(name, 'r') as f:
        return np.array([[int(i) for i in line.strip()] for line in f.readlines()])


def check_left(i: int, j: int, cave_map: np.array) -> bool:
    return cave_map[i, j - 1] > cave_map[i, j] if j != 0 else True


def check_right(i: int, j: int, cave_map: np.array) -> bool:
    if j == len(cave_map[i]) - 1:
        return True

    return cave_map[i, j + 1] > cave_map[i, j]


def check_down(i: int, j: int, cave_map: np.array) -> bool:
    if i == len(cave_map) - 1:
        return True

    return cave_map[i + 1, j] > cave_map[i, j]


def check_up(i: int, j: int, cave_map: np.array) -> bool:
    return cave_map[i - 1, j] > cave_map[i, j] if i != 0 else True


def find_local_lows(cave_floor: np.array) -> list:
    directions = {
        'left': check_left,
        'right': check_right,
        'down': check_down,
        'up': check_up
    }

    lows = []

    for i, horizontal in enumerate(cave_floor):
        for j, vertical in enumerate(horizontal):
            if np.array([directions[k](i, j, cave_floor) for k in directions]).all():
                lows.append([i, j])

    return lows
if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    cave_floor = read_input(RAW_INPUT)
    lows = find_local_lows(cave_floor)

    print(' Part One '.center(30, '*'))
    print(f'There are a total of {len(lows)} and the sum of their risk levels are {sum([cave_floor[i, j] + 1 for i, j in lows])}')