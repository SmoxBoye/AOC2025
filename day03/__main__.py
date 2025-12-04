from utility.timer import aoc_timed


def read_data(path):
    with open(path, "r") as f:
        file = f.readlines()

    data = list(map(str.strip, file))
    data = [list(map(int, "".join(line))) for line in data]
    return data


@aoc_timed
def part1(data: list[list[int]]):
    sum = 0
    for bank in data:
        highest = 0  # Lowest "joltage" is 1 so zero is fine here
        search_index = 0

        bank_len = len(bank)
        for i, bat in enumerate(bank):
            if bat == 9:
                highest = 9
                search_index = i
                break
            if bat > highest:
                highest = bat
                search_index = i
            if i == bank_len - 2:
                break
        highest2 = 0
        for i in range(search_index + 1, bank_len):
            if bank[i] > highest2:
                highest2 = bank[i]

        joltage = highest * 10 + highest2

        sum += joltage

    return sum


@aoc_timed
def part2(data: list[list[int]]):
    final = 0
    for bank in data:
        batteries = []
        search_index = 0
        bank_len = len(bank)
        for count in range(12):
            highest = 0  # Lowest "joltage" is 1 so zero is fine here
            highest_index = 0
            for i in range(search_index, bank_len - (11 - count)):
                bat = bank[i]
                if bat == 9:
                    highest_index = i + 1
                    highest = bat
                    break
                if bat > highest:
                    highest = bat
                    highest_index = i + 1
            batteries.append(highest)
            search_index = highest_index

        batteries.reverse()
        joltage = int(sum([bat * 10**i for i, bat in enumerate(batteries)]))
        final += joltage

    return final


if __name__ == "__main__":
    res1 = part1(read_data("day03/data.txt"))
    print(f"Part1: {res1}")
    res2 = part2(read_data("day03/data.txt"))
    print(f"Part 2: {res2}")
