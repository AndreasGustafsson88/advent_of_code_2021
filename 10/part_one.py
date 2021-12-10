######################
# December 10th, Part 1
######################


def read_input(name: str) -> list:
    with open(name, 'r') as f:
        return [line.strip() for line in f.readlines()]


def check_balance(d):
    for v in d.values():
        if v < 0:
            return True
    return False


def find_syntax_errors(chunks:list) -> list:

    e = []
    for chunk in chunks:
        errors = []
        open_brackets = []
        bracket_pairs = [['<', '>'], ['(', ')'], ('[', ']'), ('{', '}')]
        openings = [v[0] for v in bracket_pairs]
        reciprocal = {v[1]: v[0] for v  in bracket_pairs}
        for char in chunk:
            if char in openings:
                open_brackets.append(char)
            else:
                if open_brackets[-1] != reciprocal[char]:
                    errors.append(char)
                    open_brackets.pop(-1)
                else:
                    open_brackets.pop(-1)
        e.append(errors)
    return e

if __name__ == "__main__":
    error_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    RAW_INPUT = 'input.txt'

    chunks = read_input(RAW_INPUT)
    errors = find_syntax_errors(chunks)

    print(' Part One '.center(30, '*'))
    print(f'The total syntax error score is {sum([error_points[e[0]] for e in errors if e])}')
