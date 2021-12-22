#######################
# December 19th, Part 1
#######################

from part_one import read_input, get_overlapping_beacons
from itertools import combinations


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    scanner_results = read_input(RAW_INPUT)
    _, known_pos = get_overlapping_beacons(scanner_results)

    print(' Part One '.center(30, '*'))
    print(f'The max distance between two scanners are {max(map(lambda x: abs(sum([x[0][i]-x[1][i] for i in range(3)])), combinations(known_pos.values(), 2)))}')