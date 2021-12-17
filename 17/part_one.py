#######################
# December 17th, Part 1
#######################


def highest_y(y_low):
    """No need to consider x since we can stall a shot that dx=0 within target area."""
    return y_low * (y_low + 1) // 2


if __name__ == "__main__":
    RAW_INPUT = 'test_input.txt'

    print(' Part One '.center(30, '*'))
    print(f'The highest y is {highest_y(-142)}')
