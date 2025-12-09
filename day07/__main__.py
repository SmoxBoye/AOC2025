from utility.timer import aoc_timed


def read_data(path, part1):
    with open(path, "r") as f:
        file = f.readlines()

    data = list(map(str.strip, file))

    start = None
    diagram = {}

    for y, line in enumerate(data):
        for x, value in enumerate(line):
            if value == "S":
                start = (x, y)
            elif value == "^":
                if part1:
                    diagram[(x, y)] = False
                else:
                    diagram[(x, y)] = []
    return start, diagram, (len(data[0]), len(data))


@aoc_timed
def part1(start, diagram: dict, dim):

    queue = [start]

    # Work our way down the tachyon manifolds
    while queue:
        beam = queue.pop(0)
        x = beam[0]
        for y in range(beam[1], dim[1]):
            if (x, y) in diagram:
                # If it already split once we don't need to go again
                if diagram[(x, y)]:
                    break

                queue.append((x - 1, y))
                queue.append((x + 1, y))
                diagram[(x, y)] = True
                break

    # Count the hits
    count = 0
    for i in diagram.values():
        if i:
            count += 1

    return count


@aoc_timed
def part2(start, diagram: dict, dim):

    # Initial beam
    for y in range(start[1], dim[1]):
        if (start[0], y) in diagram:
            diagram[(start[0], y)].append(1)
            break

    manifolds = sorted(list(diagram.keys()), key=lambda coord: (coord[1], coord[0]))

    count = 0
    for x, y in manifolds:
        if (x, y) in diagram:
            # If the manifold never got hit we can ignore it
            if not diagram[(x, y)]:
                continue
            current = sum(diagram[(x, y)])

            for dir in [-1, 1]:
                y_beam = y
                while y_beam < dim[1]:
                    if (x + dir, y_beam) in diagram:
                        diagram[(x + dir, y_beam)].append(current)
                        break
                    y_beam += 1

                    # Add beam if we hit the end
                    if y_beam == dim[1]:
                        count += current

    return count


if __name__ == "__main__":
    res1 = part1(*read_data("day07/data.txt", True))
    print(f"Part 1: {res1}")
    res2 = part2(*read_data("day07/data.txt", False))
    print(f"Part 2: {res2}")
