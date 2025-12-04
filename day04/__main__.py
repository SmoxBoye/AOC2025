from utility.timer import aoc_timed


def read_data(path):
    with open(path, "r") as f:
        file = f.readlines()

    data = list(map(str.strip, file))
    data = [[point == "@" for point in "".join(line)] for line in data]

    return data


def get_point(data, p):
    if p[0] < 0 or p[0] >= len(data[0]):
        return False
    if p[1] < 0 or p[1] >= len(data):
        return False
    return data[p[1]][p[0]]


sur = []
for i in [0, -1, 1]:
    for j in [0, -1, 1]:
        sur.append((i, j))
sur.remove((0, 0))  # Could do pop(0) but w/e


def v_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def count_surrounding(data, x, y):
    count = 0

    for p in sur:
        if get_point(data, v_add(p, (x, y))):
            count += 1

    return count


@aoc_timed
def part1(data: list[list[bool]]):
    res = 0
    for y, line in enumerate(data):
        for x, p in enumerate(line):
            if p and count_surrounding(data, x, y) < 4:
                res += 1

    return res


# Comment after finishing part 2: Wow that took less time than i expected.
@aoc_timed
def part2(data: list[list[bool]]):
    res = 0
    removing = True
    while removing:
        removing = False
        for y, line in enumerate(data):
            for x, p in enumerate(line):
                if p and count_surrounding(data, x, y) < 4:
                    res += 1
                    removing = True
                    data[y][x] = False

    return res


if __name__ == "__main__":
    res1 = part1(read_data("day04/data.txt"))
    print(f"Part1: {res1}")
    res2 = part2(read_data("day04/data.txt"))
    print(f"Part 2: {res2}")
