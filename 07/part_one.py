######################
# December 7th, Part 1
######################

def read_input(name: str) -> list:
    with open(name, 'r') as f:
        return [int(line) for line in f.read().split(',')]


def find_h_moves(positions: list) -> list:
    """Returns a list of all moves required from every position"""

    return [[(abs(nr - i)) for nr in positions] for i in range(max(positions))]


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    crab_pos = read_input(RAW_INPUT)
    fuel_consumption = find_h_moves(crab_pos)
    least_moves = min(list(map(lambda x: sum(x), fuel_consumption)))

    print(' Part One '.center(30, '*'))
    print(f'The most fuel efficient move costs {least_moves} units of fuel for the crab army')
