######################
# December 8th, Part 2
######################

from part_one import read_input


def find_by_len(s: list, l: int) -> str:
    """Returns string based on matching len (l)."""
    return [s.pop(s.index(seq)) for seq in s if len(seq) == l][0]


def find_three(s: list, one: str) -> str:
    """Returns nr three based on len 5 and complete match on intersection on nr 1"""
    for seq in s:
        if len(seq) == 5 and set(seq).intersection(set(one)) == set(one):
            return s.pop(s.index(seq))


def find_six(s: list, one: str) -> str:
    """Returns nr six based on len 6 and one match in nr 1"""
    for seq in s:
        if len(seq) == 6 and len(set(seq).intersection(set(one))) == 1:
            return s.pop(s.index(seq))


def find_nine(s: list, four: str) -> str:
    """Returns nr 9 based on len 6 and complete matched intersection with nr 4"""
    for seq in s:
        if len(seq) == 6 and set(seq).intersection(set(four)) == set(four):
            return s.pop(s.index(seq))


def find_two(s: list, six: str) -> str:
    """Returns nr 2 based on 1 difference with nr six."""
    return [s.pop(s.index(seq)) for seq in s if len(set(seq).difference(set(six))) == 1][0]


def find_all_numbers(s: list) -> dict:
    """Calls each individual nr decipher, returns deciphered numbers in dict"""
    one, seven, four, eight = [find_by_len(s, i) for i in [2, 3, 4, 7]]
    three = find_three(s, one)
    six = find_six(s, one)
    nine = find_nine(s, four)
    zero = [s.pop(s.index(seq)) for seq in s if len(seq) == 6][0]
    two = find_two(s, six)
    five = s[0]

    return {i: val for i, val in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}


def map_numbers(segments: list) -> list:
    """Loops through all segments and maps all numbers then append and returns list of all unique mappings"""
    all_mappings = []
    for s in segments:
        numbers = find_all_numbers(s)
        all_mappings.append(numbers)

    return all_mappings


def decipher_output(outputs: list, mappings: list):
    """Iterates over every output and then check for complete match with value in mapping, appends key int(nr)"""
    deciphered = []
    for output, mapping in zip(outputs, mappings):
        nrs = [k for o in output for k, v in mapping.items() if sorted(o) == sorted(v)]
        deciphered.append(nrs)
    return deciphered

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    segments, outputs = read_input(RAW_INPUT)
    numbers_mapping = map_numbers(segments)
    deciphered_output = decipher_output(outputs, numbers_mapping)

    print(' Part Two '.center(30, '*'))
    print(f'The total sum of all added outputs are {sum([int("".join([f"{i}" for i in nr])) for nr in deciphered_output])}')