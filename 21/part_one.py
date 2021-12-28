#######################
# December 21th, Part 1
#######################


class Dice:

    def __init__(self):
        self.number = 0
        self.rolls = 0

    def roll(self):
        self.number += 1
        self.rolls += 1
        return self.number


class Player:

    def __init__(self, name, starting_pos):
        self.name = name
        self.pos = int(starting_pos)
        self.score = 0

    def roll_dice(self, dice):
        movement = sum(dice.roll() for _ in range(3))
        self.pos = (self.pos + movement) % 10
        self.score += self.pos if self.pos else 10

    @property
    def won(self):
        return self.score >= 1000


def read_input(name):
    with open(name, 'r') as f:
        return f.read().splitlines()


def play_game(players, dice):

    playing = True
    while playing:
        for p in players:
            p.roll_dice(dice)
            if p.won:
                playing = False
                print(p.score)
                break

    print(dice.rolls)
    for p in players:
        print(p.score * dice.rolls)


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    p_1, p_2 = read_input(RAW_INPUT)

    print(' Part One '.center(30, '*'))
    score = play_game((Player("Andreas", p_1[-1]), Player("Cicci", p_2[-1])), Dice())
