#######################
# December 22th, Part 2
#######################

from part_one import read_input


class Instruction:

    def __init__(self, state, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max
        self.state = state

    def __repr__(self):
        return f'{self.state}: {self.x_min}..{self.x_max}, {self.y_min}..{self.y_max}, {self.z_min}..{self.z_max}'

    def subtract(self, other):
        if not self == other:
            return [self]
        elif other.contains(self):
            return []

        cubes = []

        xs = sorted((self.x_min, self.x_max, other.x_min, other.x_max))
        ys = sorted((self.y_min, self.y_max, other.y_min, other.y_max))
        zs = sorted((self.z_min, self.z_max, other.z_min, other.z_max))

        for x0, x1 in zip(xs, xs[1:]):
            for y0, y1 in zip(ys, ys[1:]):
                for z0, z1 in zip(zs, zs[1:]):
                    cube = Instruction(1, x0, x1, y0, y1, z0, z1)
                    if self.contains(cube) and cube != other:
                        cubes.append(cube)
        return cubes

    def nr_lights(self):
        return (self.x_max - self.x_min) * (self.y_max - self.y_min) * (self.z_max - self.z_min)

    def contains(self, other):
        return (
                self.x_min <= other.x_min and
                self.x_max >= other.x_max and
                self.y_min <= other.y_min and
                self.y_max >= other.y_max and
                self.z_min <= other.z_min and
                self.z_max >= other.z_max
        )

    def __eq__(self, other):
        return (
                self.x_min <= other.x_max - 1 and
                self.x_max - 1 >= other.x_min and
                self.y_min <= other.y_max - 1 and
                self.y_max - 1 >= other.y_min and
                self.z_min <= other.z_max - 1 and
                self.z_max - 1 >= other.z_min
        )


class Reactor:

    def __init__(self):
        self.instr = []
        self.blocks = []
        self.lights = 0

    def turn_on(self, i):

        self.blocks = [part for cube in self.blocks for part in cube.subtract(i)]

        if i.state:
            self.blocks.append(i)

    def follow_instruction(self):
        while self.instr:
            i = self.instr.pop(0)
            self.turn_on(i)

    def count_lights(self):
        return sum([b.nr_lights() for b in self.blocks])


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    input = read_input(RAW_INPUT)

    reactor = Reactor()
    reactor.instr = [Instruction(inst[0], inst[1][0], inst[1][1] + 1, inst[2][0], inst[2][1] + 1, inst[3][0], inst[3][1] + 1) for inst in input]
    reactor.follow_instruction()

    print(' Part Two '.center(30, '*'))
    print(f'Number of nodes illuminated {reactor.count_lights()}')
