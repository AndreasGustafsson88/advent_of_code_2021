#######################
# December 16th, Part 2
#######################
from functools import reduce
from part_one import read_input, dechifer_code


def get_literal_vals(p):

    if p.type == 0:
        return sum([get_literal_vals(i) for i in p.packets])
    elif p.type == 4:
        return p.literal_val
    elif p.type == 1:
        return reduce(lambda a, b: a * b, [get_literal_vals(i) for i in p.packets])
    elif p.type == 2:
        return min([get_literal_vals(i) for i in p.packets])
    elif p.type == 3:
        return max([get_literal_vals(i) for i in p.packets])
    elif p.type == 5:
        return get_literal_vals(p.packets[0]) > get_literal_vals(p.packets[1])
    elif p.type == 6:
        return get_literal_vals(p.packets[0]) < get_literal_vals(p.packets[1])
    elif p.type == 7:
        return 1 if get_literal_vals(p.packets[0]) == get_literal_vals(p.packets[1]) else 0


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    enc = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    hexa_code = read_input(RAW_INPUT)
    sequence = ''.join([enc[val] for val in hexa_code[0]])

    _, p = dechifer_code(sequence)
    m = get_literal_vals(p)
    print(' Part Tne '.center(30, '*'))
    print(f'The sum of all version packets are {m}')
