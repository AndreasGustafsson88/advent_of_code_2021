######################
# December 11th, Part 2
######################

from part_one import Octopus, Cave, read_input

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    octopus_pattern = read_input(RAW_INPUT)
    octopuses = [Octopus([i, j], octopus_pattern[i][j]) for i, line in enumerate(octopus_pattern) for j, nr in
                 enumerate(line)]
    cave = Cave(octopuses, (10, 10))

    while True:
        cave.step()
        if cave.all_flashed():
            break

    print(' Part Two '.center(30, '*'))
    print(f'After {cave.nr_step} steps all octopus flashed simultaneously')
