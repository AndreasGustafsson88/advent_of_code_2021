######################
# December 2nd, Part 1
######################

RAW_INPUT = 'input.txt'


def read_input(name: str) -> list:
    """Reads input in as nested list in format [[direction, distance]]"""

    with open(name, 'r') as f:
        return [[x, int(y)] for line in f.readlines() for x, y in zip(*line.split())]


def move_submarine(m: list, x=0, y=0) -> tuple:
    """Iterate over movements and first checks for x or y, then increase or decrease dis depending on u or, d"""

    for d, dis in m:
        if d == 'f':
            x += dis
        else:
            y += dis if d == 'd' else dis * -1

    return x, y


if __name__ == '__main__':
    movements = read_input(RAW_INPUT)
    x_pos, y_pos = move_submarine(movements)

    print(' Part One '.center(30, '*'))
    print(f'The total movement is {x_pos * y_pos}')
