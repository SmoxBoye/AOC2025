from time import time


def aoc_timed(func):
    def wrapper(*args, **kwargs):
        before = time()
        res = func(*args, **kwargs)
        after = time()
        if (
            after - before > 15.0
        ):  # AOC claims all puzzles should be able to be solved under 15 seconds. So im making it a requirement.
            print(f"Time failed! {after - before:.2f}s")
        else:
            print(f"Time passed! {after - before:.5f}s")
        return res

    return wrapper
