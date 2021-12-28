#######################
# December 21th, Part 2
#######################
from collections import defaultdict
from functools import lru_cache
from part_one import read_input


@lru_cache(maxsize=None)
def play_game(p1, s1, p2, s2):
    if s2 >= 21:
        return 0, 1

    wins_p1 = wins_p2 = 0

    for move, frequency in roll_fr.items():
        new_pos = (p1 + move) % 10 or 10
        c2, c1 = play_game(p2, s2, new_pos, s1 + new_pos)
        wins_p1 += c1 * frequency
        wins_p2 += c2 * frequency

    return wins_p1, wins_p2


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'

    roll_fr = defaultdict(int)
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                roll_fr[sum([i, j, k])] += 1

    p_1, p_2 = read_input(RAW_INPUT)
    scores = play_game(int(p_1[-1]), 0, int(p_2[-1]), 0)

    print(' Part Two '.center(30, '*'))
    print(f'The winner won in {max(scores)} nr of universes!')