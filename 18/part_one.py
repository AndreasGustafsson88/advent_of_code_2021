#######################
# December 18th, Part 1
#######################
import ast
import math


def read_input(name):
    with open(name, 'r') as f:
        return [ast.literal_eval(line.strip()) for line in f.readlines()]


class SnailNr:

    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

    def explode(self):
        return self.depth >= 5

    def split(self):
        return self.value >= 10

    def __repr__(self):
        return f'{self.value}, D:{self.depth}'


def read_list(L, i=1, nrs=None):
    if i == 1:
        nrs = []
    for j, nr in enumerate(L):
        if isinstance(nr, list):
            read_list(nr, i + 1, nrs)
        else:
            nrs.append(SnailNr(nr, i))
    return nrs


def exploding(snail_list):
    for snail in snail_list:
        if snail.explode():
            return 'explode'
    for snail in snail_list:
        if snail.split():
            return 'split'
    return False


def explode(snail_list):
    for i, snail in enumerate(snail_list):
        if snail.depth >= 5:
            x = snail.value
            y = snail_list[i + 1].value
            if i != 0:
                snail_list[i - 1].value += x
            if i != len(snail_list) - 2:
                snail_list[i + 2].value += y
            snail_list.insert(i + 1, SnailNr(0, depth=snail.depth - 1))
            snail_list.pop(i)
            snail_list.pop(i + 1)
            return


def split(snail_list):
    for i, snail in enumerate(snail_list):
        if snail.value >= 10:
            x = SnailNr(value=math.floor(snail.value / 2), depth=snail.depth + 1)
            y = SnailNr(value=math.ceil(snail.value / 2), depth=snail.depth + 1)

            snail_list.pop(i)
            snail_list.insert(i, x)
            snail_list.insert(i + 1, y)
            return


def sum_snailfish(nrs):
    snail_list = read_list(nrs.pop(0))
    while nrs:

        add_nrs = read_list(nrs.pop(0))
        snail_list.extend(add_nrs)
        for snail in snail_list:
            snail.depth += 1

        operating = True

        while operating:
            operating = False
            operation = exploding(snail_list)
            if operation == 'explode':
                explode(snail_list)
                operating = True
            elif operation == 'split':
                split(snail_list)
                operating = True
                
    return snail_list


def calc_magnitude(nrs):
    altering = True
    while altering:
        altering = False
        for i, nr in enumerate(nrs):
            if i != len(nrs) - 1:
                if nr.depth == nrs[i + 1].depth:
                    new_val = 3 * nr.value + 2 * nrs[i + 1].value
                    nrs.pop(i)
                    nrs.insert(i, SnailNr(value=new_val, depth=nr.depth - 1))
                    nrs.pop(i + 1)
                    altering = True
                    break

    return nrs[0].value

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    snail_numbers = read_input(RAW_INPUT)
    summed_snailnumber = sum_snailfish(snail_numbers)

    magnitude = calc_magnitude(summed_snailnumber)

    print(' Part One '.center(30, '*'))
    print(f'The total magnitude of the snailfish numbers are {magnitude}')