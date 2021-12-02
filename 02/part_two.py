######################
# December 2nd, Part 2
######################

from part_one import read_input

RAW_INPUT = 'input.txt'


class Submarine:
    """
    Main class for santas submarine
    """

    def __init__(self):
        self.x_pos: int = 0
        self.y_pos: int = 0
        self.aim: int = 0

    @property
    def total_pos(self) -> int:
        """Calc total post by multiplying x and y pos"""
        return self.y_pos * self.x_pos

    def move_submarine(self, m) -> None:
        """Iterate over movements and first checks for x or y, then increase or decrease dis depending on u or, d"""
        for d, dis in m:
            if d == 'f':
                self.x_pos += dis
                self.y_pos += self.aim * dis
            else:
                self.aim += dis if d == 'd' else dis * -1


if __name__ == '__main__':
    santas_submarine = Submarine()
    santas_submarine.move_submarine(read_input(RAW_INPUT))

    print(' Part Two '.center(30, '*'))
    print(santas_submarine.total_pos)
