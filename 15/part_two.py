#######################
# December 15th, Part 1
#######################

import numpy as np
from part_one import read_input, search_cave


def increase_cave_size(m):
    m = np.concatenate([m + i for i in range(5)], axis=0)
    m = np.concatenate([m + i for i in range(5)], axis=1)
    m = m % 9
    m[m == 0] = 9
    return m

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    cave_map = read_input(RAW_INPUT)
    big_cave = increase_cave_size(cave_map)
    path = search_cave(big_cave)
    print(' Part One '.center(30, '*'))
    print(f'The path with the lowest risk factor sums up to: {path}, Using Djikstra')
