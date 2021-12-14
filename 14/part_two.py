#######################
# December 14th, Part 2
#######################

from part_one import read_input


def run_polymer_template(seq, instr, run_times):
    formula_pairs = [seq[i: i + 2] for i in range(len(seq) - 1)]
    combinations = {k: 1 for k, v in instr.items() if k in formula_pairs}
    letters = combinations.copy()

    for _ in range(run_times):
        for l in letters:
            if instr.get(l, 0):
                A, B = l[0] + instr.get(l), instr.get(l) + l[1]
                if combinations.get(A):
                    combinations[A] += letters[l]
                else:
                    combinations[A] = letters[l]
                if combinations.get(B):
                    combinations[B] += letters[l]
                else:
                    combinations[B] = letters[l]
            combinations[l] -= letters[l]
        letters = combinations.copy()
    return letters


def count_letters(formula, a={}):
    for k, v in formula.items():
        if a.get(k[0]):
            a[k[0]] += v
        else:
            a[k[0]] = v
    a[start_seq[-1]] += 1
    return a


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    start_seq, instructions = read_input(RAW_INPUT)
    polymer_formula = run_polymer_template(start_seq, instructions, 40)
    letter_count = count_letters(polymer_formula)

    print(' Part Two '.center(30, '*'))
    print(f'There are {max(letter_count.values()) - min(letter_count.values())} units of values something something')
