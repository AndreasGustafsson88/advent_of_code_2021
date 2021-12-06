######################
# December 6th, Part 2
######################

from part_one import read_input


def add_initial_fish(fish):
    school_of_fish = {i: 0 for i in range(9)}

    for f in fish:
        school_of_fish[f] += 1

    return school_of_fish


def run_simulation(fish, nr_days):

    school_of_fish = add_initial_fish(fish)

    for _ in range(nr_days):
        fish_toddlers = school_of_fish[0]
        for i in range(8):
            school_of_fish[i] = school_of_fish[i + 1]
        school_of_fish[6] += fish_toddlers
        school_of_fish[8] = fish_toddlers

    return sum(school_of_fish.values())

if __name__ == "__main__":
    NR_DAYS = 256
    RAW_INPUT = 'input.txt'

    fish = read_input(RAW_INPUT)
    population = run_simulation(fish, NR_DAYS)

    print(' Part One '.center(30, '*'))
    print(f'The total size of the school of lanternfish after {NR_DAYS} is {population}')
