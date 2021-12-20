#######################
# December 18th, Part 2
#######################

from part_one import read_input, SnailNr, sum_snailfish


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


def pair_up(nrs):
    all_pairs = []
    for i, nr in enumerate(nrs):
        for j in range(len(nrs)):
            if i == j:
                continue
            else:
                all_pairs.append([nr, nrs[j]])
                all_pairs.append([nrs[j], nr])
    return all_pairs


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    snail_numbers = read_input(RAW_INPUT)
    pairs_of_snail_nrs = pair_up(snail_numbers)
    summed_snailnumber = sum_snailfish(snail_numbers)

    all_res = [sum_snailfish(list(pair)) for pair in pairs_of_snail_nrs]
    magnitudes = list(map(calc_magnitude, all_res))

    print(' Part Two '.center(30, '*'))
    print(f'The highest magnitude of the snailfish numbers are {max(magnitudes)}')