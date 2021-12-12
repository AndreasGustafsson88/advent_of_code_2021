######################
# December 11th, Part 1
######################


class Cave:

    def __init__(self, octopuses, grid_size):
        self.octopuses = octopuses
        self.grid_size = grid_size
        self.flashed = []
        self.nr_step = 0

    def get_one(self, pos):
        return list(filter(lambda x: x.pos == pos, self.octopuses))[0]

    def step(self):
        self.nr_step += 1
        c = [o.pos for o in self.octopuses]
        self.flashed = []
        while c:
            o = self.get_one(c[0])
            n, f = o.step()
            if n:
                self.flashed.append(f)
                [c.append(m) for m in n if m not in self.flashed]
                c.pop(0)
                c = [a for a in c if a not in self.flashed]
            else:
                c.pop(0)

    def sum_flashes(self):
        return sum([i.flashes for i in self.octopuses])

    def all_flashed(self):
        return sorted(self.flashed) == sorted([i.pos for i in self.octopuses])


class Octopus:

    def __init__(self, pos, nr):
        self.pos = pos
        self.nr = nr
        self.neighbours = [[i, j] for i in range(max(0, self.pos[0] - 1), min(10, self.pos[0] + 2)) for j in range(max(0, self.pos[1] - 1), min(10, self.pos[1] + 2))]
        self.flashes = 0

    def step(self):
        self.nr += 1

        if self.nr >= 10:
            self.flashes += 1
            self.nr = 0
            return self.neighbours, self.pos

        return False, False


def read_input(name: str):
    with open(name, 'r') as f:
        return [[int(i) for i in line.strip()] for line in f.readlines()]


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    NR_STEPS = 100

    octopus_pattern = read_input(RAW_INPUT)
    octopuses = [Octopus([i, j], octopus_pattern[i][j]) for i, line in enumerate(octopus_pattern) for j, nr in enumerate(line)]
    cave = Cave(octopuses, (10, 10))

    for _ in range(NR_STEPS):
        cave.step()

    print(' Part One '.center(30, '*'))
    print(f'There are {cave.sum_flashes()} nr of flashes after {NR_STEPS}')