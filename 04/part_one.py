######################
# December 4th, Part 1
######################

import numpy as np

RAW_INPUT = 'input.txt'


def read_input(name):
    """Reads input and returns all input numbers separate, and all boards as np arrays"""
    with open(name, 'r') as f:
        nrs = [int(nr) for nr in f.readline().split(',')]  # nrs

        # Get all boards and convert to int
        all_boards = [line.strip() for line in f.readlines() if len(line) > 1]
        boards = [[int(nr) for nr in line.split()] for line in all_boards]

        # Transform to np_arrays
        numpy_boards = [np.array(boards[i:i + 5]) for i in range(0, len(all_boards), 5)]

        return nrs, numpy_boards


def mark_number(nr: int, boards: list) -> None:
    """Change the current number to -1"""
    for b in boards:
        b[b == nr] = -1


def check_winner(boards: list, nr: int):
    """check if any column or row adds to -5, if so return the sum * last number"""
    for b in boards:
        if np.any(b.sum(axis=0) == -5) or np.any(b.sum(axis=1) == -5):
            return sum(b[b > 0]) * nr
    return False


def play_bingo(nrs: list, boards: list):
    """
    First mark current number for all boards to -1, to then be able to check for a total sum of -5 in any row or column.
    When a board has -5 sum all numbers that are greater than 0 and return the array * prev number.
    """

    for nr in nrs:
        mark_number(nr, boards)
        winner = check_winner(boards, nr)
        if winner:
            return winner

if __name__ == "__main__":

    numbers, np_boards = read_input(RAW_INPUT)
    winning_board = play_bingo(numbers, np_boards)

    print(' Part One '.center(30, '*'))
    print(f'The winning board has a total sum of {winning_board}')
