######################
# December 4th, Part 2
######################

import numpy as np
from part_one import read_input, mark_number

RAW_INPUT = 'input.txt'


def remove_winners(boards: list, nr: int):
    """
    check if any column or row adds to -5, if so sets all numbers to 0,
    return all boards that have a sum greater than 0. Returns sum * prev number
    if only one board left.
    """
    for b in boards:
        if np.any(b.sum(axis=0) == -5) or np.any(b.sum(axis=1) == -5):
            if len(boards) == 1:
                return sum(b[b > 0]) * nr
            else:
                b[b >= -1] = 0

    return [b for b in boards if b.sum() > 0]


def loose_at_bingo(numbers: list, boards: np.array) -> int:
    """
    Iterates over number until 1 board is left in the list and has a winning row or column.
    """
    for nr in numbers:
        mark_number(nr, boards)
        boards = remove_winners(boards, nr)

        if isinstance(boards, np.int32):
            return boards

if __name__ == "__main__":
    nrs, np_boards = read_input(RAW_INPUT)
    loosing_board = loose_at_bingo(nrs, np_boards)

    print(' Part Two '.center(30, '*'))
    print(f'The loosing board has a total sum of {loosing_board}')
