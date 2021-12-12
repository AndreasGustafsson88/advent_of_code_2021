######################
# December 12th, Part 2
######################

from collections import Counter
from part_one import read_input


def check_max_twice(new_path, routing):
    count_lower = Counter([n for n in new_path if n.islower()])
    count_lower[routing] += 1
    nr_count = Counter([v for v in count_lower.values()])

    if nr_count[2] == 2 or nr_count.get(3):
        return False

    return True


def map_all_paths(cave_mapping: dict):
    routes = []
    explored_routes = [['start']]

    while explored_routes:
        new_path = explored_routes[0]
        for routing in cave_mapping[new_path[-1]]:
            if routing.islower() and routing != 'end':
                if check_max_twice(new_path, routing):
                    explored_routes.append(new_path + [routing])
            else:
                explored_routes.append(new_path + [routing])

            if routing == 'end':
                routes.append(new_path + [routing])
                explored_routes.remove(new_path + [routing])
        explored_routes.remove(new_path)

    return routes


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    cave_mapping = read_input(RAW_INPUT)
    possible_combinations = map_all_paths(cave_mapping)

    print(' Part One '.center(30, '*'))
    print(f'There are {len(possible_combinations)} of possible paths')

