#######################
# December 14th, Part 1
#######################
from collections import Counter


def read_input(name: str):
    with open(name, 'r') as f:
        seq, instr = f.read().strip().split('\n\n')
        instr = {i[:2]: i[-1] for i in instr.split('\n')}
        return seq, instr


def run_polymer_template(seq, instr, run_times):

    for _ in range(run_times):
        formula_pairs = [seq[i: i + 2] for i in range(len(seq) - 1)]
        new_formula = [i[0] + instr[i] if i in list(instr.keys()) else i[:2] for i in formula_pairs[:-1]]
        end = [formula_pairs[-1][0] + instr[formula_pairs[-1]] + formula_pairs[-1][1] if formula_pairs[-1] in list(instr.keys()) else formula_pairs[-1][:2]]
        seq = "".join(new_formula + end)

    return seq

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    start_seq, instructions = read_input(RAW_INPUT)
    polymer_formula = run_polymer_template(start_seq, instructions, 10)

    print(' Part One '.center(30, '*'))
    print(f'There are {max(Counter(polymer_formula).values()) - min(Counter(polymer_formula).values())} units of values something something')
