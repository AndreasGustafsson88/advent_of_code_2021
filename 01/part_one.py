########
# Part 1
########

RAW_INPUT = 'input.txt'


def read_input(name: str) -> list[int]:
    """Reads input and converts to int"""

    with open(name, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def count_depth_increase(sonar_sweep: list[int]) -> int:
    """Return length of list that only accepts numbers that are higher than previous"""

    return len([a for i, a in enumerate(sonar_sweep) if a > sonar_sweep[i - 1]])


if __name__ == '__main__':
    answer = count_depth_increase(read_input(RAW_INPUT))

    print(' Part One '.center(30, '*'))
    print(f'There are a total of {answer} depth increases that the sonar finds.')
