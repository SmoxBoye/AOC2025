from collections import namedtuple
from utility.timer import aoc_timed

Keycode = namedtuple("Keycode", ["rot", "distance"])


def read_data(path):
    with open(path, "r") as f:
        data = f.readlines()

    data = list(map(str.strip, data))
    data = [
        Keycode(rot=1 if line[0] == "R" else -1, distance=int(line[1:]))
        for line in data
    ]
    return data


@aoc_timed
def part1(data: list[Keycode]):
    point = 50
    zero_count = 0
    for key in data:
        point += key.rot * key.distance

        point %= 100

        if point == 0:
            zero_count += 1

    return zero_count


# Naive solution going step by step
@aoc_timed
def part2(data: list[Keycode]):
    point = 50
    zero_count = 0
    for key in data:
        steps = key.distance
        while steps != 0:
            steps -= 1
            point += key.rot
            if point > 99:
                point = 0
            elif point < 0:
                point = 99

            if point == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    path = "day01/data.txt"
    res1 = part1(read_data(path))
    print("Part 1:", res1)
    res2 = part2(read_data(path))
    print("Part 1:", res2)
