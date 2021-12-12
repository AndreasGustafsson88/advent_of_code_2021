######################
# December 12th, Part 1
######################


def read_input(name: str):
    with open(name, 'r') as f:
        a_b = [line.strip().split('-') for line in f.readlines()]
        c = {}
        for comb in a_b:
            if not c.get(comb[0]):
                c[comb[0]] = [comb[1]] if comb[1] not in ['start'] else None
            else:
                c[comb[0]].append(comb[1]) if comb[1] not in ['start'] else None
            if not c.get(comb[1]):
                c[comb[1]] = [comb[0]] if comb[0] not in ['start'] else None
            else:
                c[comb[1]].append(comb[0]) if comb[0] not in ['start'] else None
        return c


def map_all_paths(cave_mapping: dict):
    routes = []
    explored_routes = [['start']]

    while explored_routes:
        new_path = explored_routes[0]
        for routing in cave_mapping[new_path[-1]]:
            if routing.islower() and routing != 'end':
                if routing not in new_path:
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
