#######################
# December 13th, Part 1 & 2
#######################
import numpy as np


def clean_i(i):
    return [line.strip('fold along ').split('=') for line in i.split('\n')]


def clean_p(p):
    return [list(map(int, line.split(','))) for line in p.split('\n')]


def read_input(name):
    with open(name, 'r') as f:
        p, i = f.read().split('\n\n')
        p = clean_p(p)
        i = clean_i(i)
        return p, i


def dot_paper(points):
    paper = np.zeros(shape=(max([p[1] for p in points]) + 1, max([p[0] for p in points]) + 1))
    for x, y in points:
        paper[y, x] += 1

    return paper


def fold_y(line, paper):
    piece = paper[int(line) + 1:, :]
    paper = paper[:int(line), :]
    return paper, np.flipud(piece)


def add_horizontal(paper, piece):
    if len(paper) >= len(piece):
        for i, line in enumerate(piece):
            paper[-i] += piece[-i]
        return paper
    else:
        for i, line in enumerate(paper):
            piece[-i] += paper[-i]
        return piece


def fold_x(line, paper):
    piece = paper[:, int(line) + 1:]
    paper = paper[:, :int(line)]
    return paper, np.fliplr(piece)


def add_vertical(paper, piece):
    if len(paper) >= len(piece):
        for i, line in enumerate(piece):
            for j, nr in enumerate(line):
                paper[i][-j] += piece[i][-j]
        return paper
    else:
        for i, line in enumerate(paper):
            for j, nr in enumerate(line):
                piece[i][-j] += paper[i][-j]
        return piece


def fold_paper(instructions, paper):
    for x_y, line in instructions:
        if x_y == 'y':
            paper, piece = fold_y(line, np.array(paper))
            paper = add_horizontal(list(paper), list(piece))
        if x_y == 'x':
            paper, piece = fold_x(line, np.array(paper))
            paper = add_vertical(list(paper), list(piece))
    return paper


def fold_transparent_paper(points, instructions):
    dotted_paper = dot_paper(points)
    return fold_paper(instructions, dotted_paper)


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    points, instructions = read_input(RAW_INPUT)
    folded_pattern = fold_transparent_paper(points, instructions)
    print(' Part Two '.center(30, '*'))
    for line in folded_pattern:
        for nr in line:
            if nr != 0:
                print('#', end="")
            else:
                print(" ", end="")
        print()
