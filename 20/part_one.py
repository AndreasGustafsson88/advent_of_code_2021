#######################
# December 20th, Part 1
#######################
import numpy as np


def read_input(name):
    with open(name, 'r') as f:
        decode, *msg = f.read().splitlines()
        msg = np.array([[1 if token == '#' else 0 for token in line] for line in msg[1:]])
        return [1 if token == '#' else 0 for token in decode], msg


def pad_img(mini_img, nr_iterated):
    return np.pad(mini_img, 2, constant_values=0) if not nr_iterated % 2 else np.pad(mini_img, 2, constant_values=1)


def enhance(a, p_img):
    h, w = p_img.shape
    new_img = p_img[1: w-1, 1:w-1].flatten()

    for i, line in enumerate(p_img[1: w-1, 1:w-1]):
        for j in range(len(line)):
            section = p_img[i:i+3, j:j+3]
            val = int(''.join(str(s) for s in section.flatten()), 2)
            new_val = a[val]
            new_img[i * (w-2) + j] = new_val

    return new_img.reshape(-1, w - 2)


def img_enhancer(algo, mini_img, iteration):

    padded_img = pad_img(mini_img, iteration)
    return enhance(algo, padded_img)

if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    NR_ENHANCED = 2
    algorithm, img = read_input(RAW_INPUT)

    for i in range(NR_ENHANCED):
        img = img_enhancer(algorithm, img, i)

    print(' Part One '.center(30, '*'))
    print(f'The number of light spots in the image are: {np.count_nonzero(img)}')
