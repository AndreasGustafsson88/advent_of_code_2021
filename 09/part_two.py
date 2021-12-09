######################
# December 9th, Part 2
######################
from functools import reduce

from part_one import read_input, find_local_lows
import numpy as np


def check_left(i, j, cave_map):
    if j == 0:
        return False
    else:
        return (i, (j - 1)) if cave_map[i, j - 1] != 9 else False


def check_right(i, j, cave_map):
    if j == len(cave_map[i]) - 1:
        return False
    else:
        return (i, (j + 1)) if cave_map[i, j + 1] != 9 else False


def check_down(i: int, j: int, cave_map: np.array) -> bool:
    if i == len(cave_map) - 1:
        return False

    return (i + 1, j) if cave_map[i + 1, j] != 9 else False


def check_up(i: int, j: int, cave_map: np.array) -> bool:
    if i == 0:
        return False

    return (i - 1, j) if cave_map[i - 1, j] != 9 else False


def find_basins(cave_floor: np.array, lows: list[list]):
    directions = {
        'left': check_left,
        'right': check_right,
        'up': check_up,
        'down': check_down
    }
    basins = []
    for low in lows:
        local_basin = []
        searching_idx = [tuple(low)]
        while searching_idx:
            idx = searching_idx[0]  # Reference index
            local_basin.append(idx)

            new_idx = [directions[k](*idx, cave_floor) for k in directions]

            for i in new_idx:
                searching_idx.append(i) if i and i not in local_basin and i not in searching_idx else None

            #  Remove recently searched idx
            searching_idx.remove(idx)

            # Check if step r, l, u, d is possible, if so append low and local. after step remove from low
        basins.append(local_basin)

    return basins

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    cave_floor = read_input(RAW_INPUT)
    lows = find_local_lows(cave_floor)

    basins = find_basins(cave_floor, lows)

    print(' Part One '.center(30, '*'))
    print(f'There are a total of {len(basins)} and the product of the tree largest are {reduce(lambda a, b: a * b, [len(i) for i in sorted(basins, key=lambda x: len(x), reverse=True)[:3]])}')
