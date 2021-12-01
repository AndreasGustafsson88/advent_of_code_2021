import time


def time_ns(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        answer = func(*args, **kwargs)
        print(f'Time: {time.time_ns() - start} {func}')
        return answer
    return wrapper
