#######################
# December 19th, Part 1
#######################

import itertools
from itertools import combinations
import numpy as np
from scipy.spatial.distance import euclidean


class Scanner:

    def __init__(self, name, values):
        self.name = name
        self.values = list(map(lambda x: list(map(int, x.split(','))), values))
        self.relative_pos = {}
        self.common_probes = {}
        self.pos_relative_probes()
        self.unique_probes = set(tuple(i) for i in self.values)

    def pos_relative_probes(self):
        for i, j in combinations(self.values, 2):
            self.relative_pos[tuple(i), tuple(j)] = euclidean(i, j)

    def pos_rel(self):
        for i, j in combinations(self.unique_probes, 2):
            self.relative_pos[tuple(i), tuple(j)] = euclidean(i, j)

    @property
    def set_pos(self):
        return set(i for i in self.relative_pos.values())

    def __eq__(self, other):
        return len(self.set_pos.intersection(other.set_pos)) >= 66


    def set_common_probes(self, other):

        common_vals = self.set_pos.intersection(other.set_pos)

        l_1 = list(filter(lambda x: x if x[1] in common_vals else None, self.relative_pos.items()))
        l_2 = list(filter(lambda x: x if x[1] in common_vals else None, other.relative_pos.items()))

        unique_1 = set(v for values in l_1 for v in values[0])
        unique_2 = set(v for values in l_2 for v in values[0])

        dist = {v: set() for v in list(unique_1) + list(unique_2)}

        for k, v in self.relative_pos.items():
            if k[0] in dist.keys():
                dist[k[0]].add(v)
            if k[1] in dist.keys():
                dist[k[1]].add(v)

        for k, v in other.relative_pos.items():
            if k[0] in dist.keys():
                dist[k[0]].add(v)
            if k[1] in dist.keys():
                dist[k[1]].add(v)

        x = [(i[0], j[0]) for i, j in combinations(dist.items(), 2) if len(i[1].intersection(j[1])) > 10]

        sign = [-1, 1]
        for i, p in enumerate(list(itertools.permutations([0, 1, 2]))):
            si = []
            for s in sign:
                if x[0][0][0] + x[0][1][p[0]] * s == x[1][0][0] + x[1][1][p[0]] * s:
                    si.append(s)
            for s in sign:
                if x[0][0][1] + x[0][1][p[1]] * s == x[1][0][1] + x[1][1][p[1]] * s:
                    si.append(s)
            for s in sign:
                if x[0][0][2] + x[0][1][p[2]] * s == x[1][0][2] + x[1][1][p[2]] * s:
                    si.append(s)
            if len(si) == 3:
                perm = si
                xyz = p
                pos = x[0][0][0] + x[0][1][xyz[0]] * perm[0], x[0][0][1] + x[0][1][xyz[1]] * perm[1], x[0][0][2] + x[0][1][xyz[2]] * perm[2]
                break

        self.append_new_probes(perm, xyz, pos, other.values)
        self.pos_rel()

        return pos

    def __repr__(self):
        return f'{self.name} {len(self.values)}'

    def append_new_probes(self, perm, xyz, ref_pos, other):
        [self.unique_probes.add(i) for i in list(map(lambda p: tuple(p), self.values))]
        others = list(map(lambda x: (ref_pos[0] + x[xyz[0]]*perm[0] *-1, ref_pos[1] + x[xyz[1]]*perm[1]*-1, ref_pos[2] + x[xyz[2]]*perm[2]*-1), other))
        [self.unique_probes.add(i) for i in others]


def read_input(name):
    with open(name, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        idx = [lines.index(val) for val in [f'--- scanner {i} ---' for i in range(0, 26)]]
        gathered = [lines[idx[i]: idx[(i + 1)]] for i in range(len(idx) - 1)]
        gathered.append(lines[idx[-1]:])
        return [Scanner(val[0], val[1:]) for val in gathered]


def get_overlapping_beacons(scanners):
    known_pos = {scanner.name: (0, 0, 0) if scanner.name == '--- scanner 0 ---' else False for scanner in scanners}
    reference = scanners.pop(0)
    while not np.array([1 if v else 0 for v in known_pos.values()], dtype=object).all():
        for scanner in scanners:
            if reference == scanner and not known_pos[scanner.name]:
                ref_pos = reference.set_common_probes(scanner)
                known_pos[scanner.name] = ref_pos

    return reference, known_pos


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    scanner_results = read_input(RAW_INPUT)
    scanner_0, _ = get_overlapping_beacons(scanner_results)

    print(' Part One '.center(30, '*'))
    print(f'There are a total of {len(scanner_0.unique_probes)} out there...')