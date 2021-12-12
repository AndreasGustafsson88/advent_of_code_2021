######################
# December 10th, Part 2
######################

from part_one import read_input, find_syntax_errors


def find_missing_brackets(chunk):
    open_brackets = []
    openings = [v[0] for v in bracket_pairs]
    [open_brackets.append(char) if char in openings else open_brackets.pop(-1) for char in chunk]

    return open_brackets


def complete_lines(chunks):
    completed_brackets = []
    reciprocal = {v[0]: v[1] for v in bracket_pairs}

    for chunk in chunks:
        unclosed_chars = find_missing_brackets(chunk)
        completed_brackets.append([reciprocal[bracket] for bracket in unclosed_chars[::-1]])

    return completed_brackets


def get_sum(line):
    total = 0
    for char in line:
        total = total * 5 + error_points[char]
    return total


def calc_values(completed_lines):
    return [get_sum(line) for line in completed_lines]

if __name__ == "__main__":
    bracket_pairs = [['<', '>'], ['(', ')'], ('[', ']'), ('{', '}')]

    error_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    RAW_INPUT = 'input.txt'

    chunks = read_input(RAW_INPUT)
    error_lines = find_syntax_errors(chunks)
    completed_lines = complete_lines([chunk for i, chunk in enumerate(chunks) if not error_lines[i]])
    error_values = calc_values(completed_lines)

    print(' Part One '.center(30, '*'))
    print(f'The middle score of the completed syntax is {sorted(error_values)[len(error_values) // 2]}')
