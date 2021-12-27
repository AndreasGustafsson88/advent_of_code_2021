#######################
# December 20th, Part 2
#######################
import numpy as np
from part_one import read_input, img_enhancer

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    NR_ENHANCED = 50

    algorithm, img = read_input(RAW_INPUT)

    for i in range(NR_ENHANCED):
        img = img_enhancer(algorithm, img, i)

    print(' Part One '.center(30, '*'))
    print(f'The number of light spots in the image are: {np.count_nonzero(img)}')
