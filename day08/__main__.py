from utility.timer import aoc_timed
import math
import heapq

# If i ever revisit this it would be cool to implement DSU

# Also this was written during the tail end of a mild migraine..


class Box:
    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __repr__(self):
        return f"Box({self.x}, {self.y}, {self.z})"


# This is 100% the type of task where the datas tructure is actually important so im leaving all the heavy work to the different parts for fun
def read_data(path):
    with open(path, "r") as f:
        file = f.readlines()

    data = list(map(str.strip, file))

    boxes = []
    for line in data:
        parts = line.split(",")
        boxes.append(Box(int(parts[0]), int(parts[1]), int(parts[2])))

    return boxes


def dist(a: Box, b: Box):
    return math.sqrt(
        math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2) + math.pow(a.z - b.z, 2)
    )


@aoc_timed
def part1(data, target_connections):

    dists = {}

    # I don't like this but the dataset is not too big so w/e
    for box in data:
        for box2 in data:
            if box == box2:
                continue

            if (box, box2) in dists or (box2, box) in dists:
                continue

            dists[(box, box2)] = dist(box, box2)

    distances = [(v, k) for k, v in dists.items()]
    heapq.heapify(distances)

    world = []
    connections = 0
    while connections < target_connections:
        group = heapq.heappop(distances)[1]

        found: list[set] = []

        for part in group:
            for box in world:
                if part in box:
                    found.append(box)
                    break
            else:  # nobreak
                found.append(set([part]))

        # This one line tripped me up so hard in the instructions..
        if found[0].intersection(found[1]):
            connections += 1
            continue

        # I hate this solution
        for f in found:
            try:
                world.remove(f)
            except:
                pass

        # Join the two sets and add them back
        found[0].update(found[1])
        world.append(found[0])

        connections += 1

    counts = []
    for line in world:
        counts.append(len(line))

    counts.sort(reverse=True)
    return counts[0] * counts[1] * counts[2]


@aoc_timed
def part2(data):

    dists = {}

    # I don't like this but the dataset is not too big so w/e
    for box in data:
        for box2 in data:
            if box == box2:
                continue

            if (box, box2) in dists or (box2, box) in dists:
                continue

            dists[(box, box2)] = dist(box, box2)

    distances = [(v, k) for k, v in dists.items()]
    heapq.heapify(distances)

    world = []
    connections = 0

    last_connections = []
    target_set = set(data)
    fully_connected = False
    while not fully_connected:
        group = heapq.heappop(distances)[1]

        found: list[set] = []

        for part in group:
            for box in world:
                if part in box:
                    found.append(box)
                    break
            else:  # nobreak
                found.append(set([part]))

        # This one line tripped me up so hard in the instructions..
        if found[0].intersection(found[1]):
            last_connections = group
            connections += 1
            continue

        # I still hate this
        for f in found:
            try:
                world.remove(f)
            except:
                pass

        # Join the two sets and add them back
        found[0].update(found[1])
        world.append(found[0])

        last_connections = group

        # If all boxes are connected
        if target_set == world[0]:
            fully_connected = True

    return last_connections[0].x * last_connections[1].x


if __name__ == "__main__":
    res1 = part1(read_data("day08/data.txt"), 1000)
    print(f"Part 1: {res1}")
    res2 = part2(read_data("day08/data.txt"))
    print(f"Part 2: {res2}")
