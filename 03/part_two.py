######################
# December 3rd, Part 2
######################

from part_one import read_input, sum_binary

RAW_INPUT = 'input.txt'


def find_most_frequent_nr(index: int, diagnostic: list) -> int:
    """Iterates over all numbers at given index pos and returns either 1 or 0 depending on which is most freq."""
    return 1 if [n[index] for n in diagnostic].count('1') >= [n[index] for n in diagnostic].count('0') else 0


def find_least_frequent_nr(index: int, diagnostic: list) -> int:
    """Iterates over all numbers at given index pos and returns either 1 or 0 depending on which is least freq."""
    return 0 if [n[index] for n in diagnostic].count('1') >= [n[index] for n in diagnostic].count('0') else 1


def remove_numbers(index: int, number: int, diagnostic: list) -> list:
    """Returns new list only containing numbers that match number at index pos"""
    return list(filter(lambda x: x if int(x[index]) == number else None, diagnostic))


def oxygen_generator_rating(diagnostic: list, oxygen) -> str:
    """
    Finds most frequent number at every index position and removes them for every iteration.
    Stops when there is only 1 sequence remaining and returns that as a str.
    """
    index = 0

    while len(diagnostic) > 1:
        target_nr = find_most_frequent_nr(index, diagnostic) if oxygen else find_least_frequent_nr(index, diagnostic)
        diagnostic = remove_numbers(index, target_nr, diagnostic)
        index += 1

    return "".join(diagnostic)


if __name__ == "__main__":
    input = read_input(RAW_INPUT)
    oxygen_rating = oxygen_generator_rating(input, oxygen=True)
    CO_2_rating = oxygen_generator_rating(input, oxygen=False)

    print(' Part One '.center(30, '*'))
    print(f'The life support rating of the submarine is: {sum_binary(oxygen_rating, CO_2_rating)} units of something')
