######################
# December 3rd, Part 1
######################

RAW_INPUT = 'input.txt'


def read_input(name):
    """Reads input in as and returns each number"""
    with open(name, 'r') as f:
        return [line.strip() for line in f.readlines()]


def rearrange_numbers(report: list) -> list:
    """Rearranges numbers to a new list with all the numbers at index pos x"""
    return [[nr[i] for nr in report] for i in range(len(report[0]))]


def get_gamma_and_epsilon(report: list[str]) -> tuple:
    """
    Get the rearranged numbers and iterates over them, checking which is most frequent and adding to gamma &
    epsilon.
    """
    summed_numbers = rearrange_numbers(report)

    g, e = "", ""
    for num in summed_numbers:
        most_freq = '1' if num.count('1') > num.count('0') else '0'
        g += most_freq
        e += '1' if most_freq == '0' else '0'

    return g, e


def sum_binary(x: str, y: str) -> int:
    return int(x, 2) * int(y, 2)

if __name__ == "__main__":
    diagnostics_report = read_input(RAW_INPUT)
    gamma, epsilon = get_gamma_and_epsilon(diagnostics_report)

    print(' Part One '.center(30, '*'))
    print(f'The power consumption of the submarine is: {sum_binary(gamma, epsilon)} units of something')
