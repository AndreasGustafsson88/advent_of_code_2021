#######################
# December 22th, Part 1
#######################

import numpy as np


def read_input(name):
    with open(name, 'r') as f:
        data = f.read().splitlines()
        lines = [d.split('=') for d in data]
        return [[1 if 'on' in l[0] else 0, list(map(int, l[1].replace(',y', '').split('..'))),
                 list(map(int, l[2].replace(',z', '').split('..'))), list(map(int, l[3].split('..')))] for l in lines]

if __name__ == "__main__":
    RAW_INPUT = 'test_input.txt'

    input = read_input(RAW_INPUT)

    reactor = np.zeros(shape=(101, 101, 101), dtype=np.uint)
    for inst in input:
        xmin, xmax, ymin, ymax, zmin, zmax = *inst[1], *inst[2], *inst[3]
        if inst[0]:
            reactor[xmin + 50: xmax + 50 + 1, ymin + 50:ymax + 50 + 1, zmin + 50: zmax + 50 + 1] = 1
        else:
            reactor[xmin + 50: xmax + 50 + 1, ymin + 50:ymax + 50 + 1, zmin + 50: zmax + 50 + 1] = 0
        print(np.count_nonzero(reactor))

    print(' Part One '.center(30, '*'))
    print(f'There are {np.count_nonzero(reactor)} number of lights in the core')
