########
# Part 2
########

from part_one import read_input, count_depth_increase

SLIDING_WINDOW = 3
RAW_INPUT = 'input.txt'


def count_sliding_window_sum(sonar_sweep: list[int]) -> list[int]:
    """Creates new list with total of numbers according to SLIDING_WINDOW, then sums that list"""

    return [sum(sonar_sweep[i - SLIDING_WINDOW: i]) for i, n in enumerate(sonar_sweep[:-2], SLIDING_WINDOW)]


if __name__ == '__main__':
    average = count_sliding_window_sum(read_input(RAW_INPUT))
    answer = count_depth_increase(average)

    print(' Part Two '.center(30, '*'))
    print(f'There are a total of {answer} depth increases that the sonar finds.')
