from collections import namedtuple
from utility.timer import aoc_timed


IDPair = namedtuple("IDPair", ["lower", "upper"])


def read_data(path):
    with open(path, "r") as f:
        data = f.read()

    data = str.split(data, ",")
    data = [str.split(id_pair, "-") for id_pair in data]
    data = [IDPair(lower=int(pair[0]), upper=int(pair[1])) for pair in data]
    return data


# Let's go with the naive solution and see if get hit by the time complexity demon
# (After finishing part 1): It's slow and cringe but I did not get hit by the demon
@aoc_timed
def part1(data: list[IDPair]):
    final = 0

    for id in data:
        low = id.lower
        upper = id.upper

        for i in range(low, upper + 1):
            i_str = str(i)
            i_len = len(i_str)
            if i_len % 2 == 0:
                first_half = i_str[: i_len // 2]
                second_half = i_str[i_len // 2 :]

                if first_half == second_half:
                    final += i

    return final


def check_substrings(full, substring):
    sub_len = len(substring)
    current = 0
    while current < len(full):
        if substring != full[current : current + sub_len]:
            return False
        current += sub_len

    return True


# Oboi substrings
# Holy unoptimal, but thats fine i guess
@aoc_timed
def part2(data: list[IDPair]):
    final = 0
    for id in data:
        low = id.lower
        upper = id.upper

        for i in range(low, upper + 1):
            i_str = str(i)
            i_len = len(i_str)
            for k in range(1, i_len // 2 + 1):
                substring = i_str[:k]
                if check_substrings(i_str, substring):
                    final += i
                    break

    return final


if __name__ == "__main__":
    res1 = part1(read_data("day02/data.txt"))
    print("Part 1:", res1)
    res2 = part2(read_data("day02/data.txt"))
    print("Part 2:", res2)
