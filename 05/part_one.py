######################
# December 5th, Part 1
######################
import numpy as np

RAW_INPUT = 'input.txt'


class Point:
    """
    Hold all information about coordinates for every point. Start / stop x and y

    if line is not a straight line, creates and appends all coordinates between start and stop to
    self.coordinates.
    """

    def __init__(self, x1, y1, x2, y2):
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2
        self.coordinates: list = []

        if not self.straight_line:
            self.create_subpoints()

    @property
    def straight_line(self) -> bool:
        """Checks if start and stop are horizontal or vertical"""
        return True if self.x1 == self.x2 or self.y1 == self.y2 else False

    def create_subpoints(self) -> None:
        """Creates all points in between start and stop in not straight line"""
        if self.x1 < self.x2:
            for i in range(self.x2 - self.x1 - 1):
                self.coordinates.append([self.x1 + i + 1, self.y1 + i + 1 if self.y1 < self.y2 else self.y1 - i - 1])
        else:
            for i in range(self.x1 - self.x2 - 1):
                self.coordinates.append([self.x1 - i - 1, self.y1 + i + 1 if self.y1 < self.y2 else self.y1 - i - 1])


def read_input(name: str) -> list:
    """Reads input and returns a list with instances of Point."""
    with open(name, 'r') as f:
        nrs = [",".join(nr) for nr in [line.strip().split('->') for line in f.readlines()]]
        return [Point(*list(map(lambda x: int(x), nr.split(',')))) for nr in nrs]


def plot_points(point: Point, board: np.array) -> np.array:
    if point.straight_line:
        board[min(point.y1, point.y2): max(point.y1, point.y2) + 1, min(point.x1, point.x2): max(point.x1, point.x2) + 1] += 1


def map_vents(points: list, size: tuple) -> np.array:
    """Creates board of selected size, then iterates over every point and calls plot_points"""
    board = np.zeros(shape=size)
    [plot_points(point, board) for point in points]
    return board

if __name__ == "__main__":
    all_points = read_input(RAW_INPUT)
    map_over_vents = map_vents(all_points, (1000, 1000))

    print(' Part One '.center(30, '*'))
    print(f'The number of times vent overlaps are {(map_over_vents >= 2).sum()} times')
