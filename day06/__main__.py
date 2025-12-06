from utility.timer import aoc_timed


def read_data1(path):
    with open(path, "r") as f:
        file = f.readlines()

    data = list(map(str.strip, file))

    data = [line.split(" ") for line in data]
    data = [list(filter(lambda x: x, line)) for line in data]
    return data


def read_data2(path):
    with open(path, "r") as f:
        file = f.readlines()

    data = [line.replace("\n", "") for line in file]

    return data


@aoc_timed
def part1(data):
    modifiers = data.pop(-1)
    data = [list(map(int, line)) for line in data]

    final = 0
    for i in range(len(data[0])):  # Assuming everything is equally long..
        partial_res = 0
        for line in data:
            if partial_res == 0:
                partial_res += line[i]
                continue

            if modifiers[i] == "+":
                partial_res += line[i]
            elif modifiers[i] == "*":
                partial_res *= line[i]

        final += partial_res
    return final


# This is so ass lmao, never want to see this ever again
@aoc_timed
def part2(data):
    horizontal_len = len(data[0])

    unfiltered_modifiers = data.pop(-1)
    modifiers = []
    for mod in unfiltered_modifiers:
        if mod != " ":
            modifiers.append(mod)

    the_big_grid = []
    # Im just gonna sweep the whole thing
    for i in range(horizontal_len):
        h_line = ""
        for line in data:
            h_line += line[i]
        the_big_grid.append(h_line)

    the_big_grid = [line.split(" ") for line in the_big_grid]
    the_big_grid = [list(filter(lambda x: x, line)) for line in the_big_grid]
    data = []
    row = []
    for num in the_big_grid:
        if num:
            row.append(int(num[0]))
        else:
            row.reverse()
            data.append(row)
            row = []
    if row:  # if it didnt end on a space add the last row
        row.reverse()
        data.append(row)

    final = 0
    for i, line in enumerate(data):  # Assuming everything is equally long..
        partial_res = 0
        for num in line:
            if partial_res == 0:
                partial_res += num
                continue

            if modifiers[i] == "+":
                partial_res += num
            elif modifiers[i] == "*":
                partial_res *= num

        final += partial_res
    return final


if __name__ == "__main__":
    res1 = part1(read_data1("day06/data.txt"))
    print(f"Part1: {res1}")
    res2 = part2(read_data2("day06/data.txt"))
    print(f"Part 2 {res2}")
