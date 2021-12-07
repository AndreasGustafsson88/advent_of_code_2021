######################
# December 7th, Part 2
######################

from part_one import read_input, find_h_moves


def adjusted_burn_rate(moves_list: list) -> int:
    """
    Finds the consecutive sum from all moves that have previously been mapped with algorithm
    n * (n + 1) / 2
    """
    return min([sum([n * (n + 1) // 2 for n in rate]) for rate in moves_list])

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    crab_pos = read_input(RAW_INPUT)
    moves = find_h_moves(crab_pos)
    fuel_consumption = adjusted_burn_rate(moves)

    print(' Part Two '.center(30, '*'))
    print(f'The most fuel efficient move costs {fuel_consumption} units of fuel for the crab army')
