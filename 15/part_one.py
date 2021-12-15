#######################
# December 15th, Part 1
#######################

import numpy as np
import heapq as hq


def read_input(name: str):
    with open(name, 'r') as f:
        return np.genfromtxt(f, dtype=int, delimiter=1)


def search_cave(matrix):
    h, w = matrix.shape
    q = [[0, [0, 0]]]
    while q:
        val, (x, y) = hq.heappop(q)
        if (x, y) == (w-1, h-1):
            return val
        for x, y in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]:
            if 0 <= x < w and 0 <= y < h and matrix[y][x] > 0:
                hq.heappush(q, [val + matrix[y][x], [x, y]])
                matrix[y][x] = -1

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    cave_map = read_input(RAW_INPUT)
    path = search_cave(cave_map)
    print(' Part One '.center(30, '*'))
    print(f'The path with the lowest risk factor sums up to: {path}, Using Djikstra')
