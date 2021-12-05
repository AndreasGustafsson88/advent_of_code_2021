######################
# December 5th, Part 2
######################
import numpy as np
from part_one import Point, read_input

RAW_INPUT = 'input.txt'


def plot_points(point: Point, board: np.array) -> np.array:
    """Plot all points"""
    if point.straight_line:
        board[min(point.y1, point.y2): max(point.y1, point.y2) + 1, min(point.x1, point.x2): max(point.x1, point.x2) + 1] += 1
    else:
        board[point.y1, point.x1] += 1
        board[point.y2, point.x2] += 1
        for c in point.coordinates:
            board[c[1], c[0]] += 1


def map_vents(points: list, size: tuple) -> np.array:
    """Creates board of selected size, then iterates over every point and calls plot_points"""
    board = np.zeros(shape=size)
    [plot_points(point, board) for point in points]
    return board


if __name__ == "__main__":
    all_points = read_input(RAW_INPUT)
    map_over_vent = map_vents(all_points, (1000, 1000))

    print(' Part Two '.center(30, '*'))
    print(f'The number of times vent overlaps are {(map_over_vent >= 2).sum()} times')
