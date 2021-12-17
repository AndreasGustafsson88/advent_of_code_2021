#######################
# December 16th, Part 1
#######################
from functools import reduce


class Packet:

    def __init__(self, version, type, packets=None, literal_val=0):
        self.version = version
        self.type = type
        if not packets:
            self.packets = []
        else:
            self.packets = packets
        self.literal_val = literal_val


def read_input(name: str):
    with open(name, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_bits(s, c, i):
    v = s[c: c + i] if i > 1 else int(s[c: c + i])
    return v


def dechifer_code(seq):
    cursor = 0
    while cursor < len(seq):
        V = int(get_bits(seq, cursor, 3), 2)
        cursor += 3
        T = int(get_bits(seq, cursor, 3), 2)
        cursor += 3
        if T == 4:
            start = 1
            value = []
            while start:
                start = get_bits(seq, cursor, 1)
                cursor += 1
                value.append(get_bits(seq, cursor, 4))
                cursor += 4
            return cursor, Packet(version=V, type=T, literal_val=int(''.join([v for v in value]), 2))
            # first scenario complete
        else:
            I = get_bits(seq, cursor, 1)
            cursor += 1
            if I:
                L = int(get_bits(seq, cursor, 11), 2)
                cursor += 11
                packets = []
                while len(packets) < L:
                    j, packet = dechifer_code(seq[cursor:])
                    packets.append(packet)
                    cursor += j

                return cursor, Packet(version=V, type=T, packets=packets)

            else:
                L = int(get_bits(seq, cursor, 15), 2)
                cursor += 15
                packets = []
                while L:
                    j, packet = dechifer_code(seq[cursor: cursor + L])
                    cursor += j
                    L -= j
                    packets.append(packet)

                return cursor, Packet(version=V, type=T, packets=packets)


def sum_version_nr(p):
    n = 0
    a_p = [p]
    while a_p:
        p = a_p.pop()
        n += p.version
        a_p += p.packets
    return n


if __name__ == "__main__":
    RAW_INPUT = 'input.txt'
    enc = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    hexa_code = read_input(RAW_INPUT)
    sequence = ''.join([enc[val] for val in hexa_code[0]])

    _, p = dechifer_code(sequence)
    n = sum_version_nr(p)

    print(' Part One '.center(30, '*'))
    print(f'The sum of all version packets are {n}')
