######################
# December 8th, Part 1
######################

def read_input(name: str):
    """splits input and returns segment and output separate."""
    with open(name, 'r') as f:
        line = [[*line.strip().split('|')] for line in f.readlines()]
        segment = [[*l[0].strip().split()] for l in line]
        output = [[*l[1].strip().split()] for l in line]

    return segment, output


def count_instances(output: list) -> list:
    """Returns all instances of output that are of length 2, 3, 4 or 7"""
    return [i for l in output for i in l if len(i) in [2, 3, 4, 7]]


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    segment, output = read_input(RAW_INPUT)
    known_instances = count_instances(output)

    print(' Part One '.center(30, '*'))
    print(f'There are {len(known_instances)} amount of known instances.')

