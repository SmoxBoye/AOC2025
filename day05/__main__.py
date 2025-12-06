from utility.timer import aoc_timed


def read_data(path):
    with open(path, "r") as f:
        file = f.readlines()

    data = list(map(str.strip, file))
    gap = False

    ranges = []
    items = []

    for row in data:

        if row == "":
            gap = True
            continue

        if gap:
            items.append(row)
        else:
            ranges.append(row)

    parsed_ranges = []
    for r in ranges:
        parts = str.split(r, "-")
        parsed_ranges.append((int(parts[0]), int(parts[1])))

    items = list(map(int, items))

    return parsed_ranges, items


def in_range(i, r):
    if (
        r[0] <= i <= r[1]
    ):  # I learned this syntax yesterday(2025-12-05) lol, no clue how I missed this.
        return True
    return False


# On the topic of absolutely nothing I need to figure out how to make black or ruff or whatever formatter im using to stop linewrapping stuff that has comments.
# The if statement on 36-38 looks horrible due to my comment and makes the comment makes less sense for that matter.


# If I REALLY wanted to make this go faster I would probably use some tree structure to make lookups faster but w/e
@aoc_timed
def part1(ranges: list[tuple[int, int]], items: list[int]):
    fresh = 0

    for item in items:
        for r in ranges:
            if in_range(item, r):
                fresh += 1
                break

    return fresh


# Comment after finishing part 2:   I'd like to combine the "merge" and "squash" passes into a single pass but it's late and time for bed. (I'm honestly surprised that it worked as two passes, kinda expected it to break at some point)
#                                   Also my variable names are so all over the place on this one. I blame that it's currently late as im typing this lmao.
@aoc_timed
def part2(ranges: list[tuple[int, int]], items):

    # Stitching ranges together into larger ones
    # If a range is completely disjoint it gets moved to a done list
    # Sorting the list after every pass makes sure it doesnt rip itself apart.
    done = []
    while ranges:
        ranges.sort(key=lambda x: x[0])

        to_merge = ranges.pop(0)

        upper = to_merge[1]
        lower = to_merge[0]
        for r in ranges:
            if in_range(upper, r):
                ranges.append((lower, r[1]))
                ranges.remove(r)
                break
        else:
            done.append(to_merge)

    # Filtering out ranges that are fully within other ranges
    squashed = []
    for squash in done:
        lower, upper = squash[0], squash[1]

        not_overshadowed = True
        for span in done:
            if span == squash:
                continue
            if in_range(lower, span) and in_range(upper, span):
                not_overshadowed = False
                break

        if not_overshadowed:
            squashed.append(squash)

    # Final count of fresh items
    fresh = 0
    for r in squashed:
        fresh += r[1] - r[0] + 1

    return fresh


if __name__ == "__main__":
    res1 = part1(*read_data("day05/data.txt"))
    print(f"Part1: {res1}")
    res2 = part2(*read_data("day05/data.txt"))
    print(f"Part 2: {res2}")


# Leaving this in as i was trying to visualise part 2

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#     -----
#                    ------|-----
#                          |           |-------------
#                          |-----------|-----
#                          |           |
#     -----          ------|-----------|-------------

# I need to detect overlapping areas so i can stitch them together.
# Then i can just do (upper - lower) to get the total fresh items for a range.
