#######################
# December 17th, Part 2
#######################


def search_x_y_vel():
    hits = 0
    for dx in range(0, 161):
        for dy in range(-143, 1000):
            x = 0
            y = 0
            DX = dx
            DY = dy
            hit = False
            for _ in range(1000):
                x += DX
                y += DY
                if 128 <= x <= 160 and -142 <= y <= -88:
                    hit = True
                    break
                if y < -142:
                    break
                if DX != 0:
                    DX -= 1
                DY -= 1
            if hit:
                hits += 1
    return hits

if __name__ == "__main__":
    RAW_INPUT = 'test_input.txt'

    print(' Part One '.center(30, '*'))
    print(f'The nr of hits could be {search_x_y_vel()}')

