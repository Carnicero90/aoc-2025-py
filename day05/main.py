import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    ranges, ids = [i.split("\n") for i in file.read().strip().split("\n\n")]

ranges = sorted([tuple(int(j) for j in i.split("-")) for i in ranges])
ids = (int(i) for i in ids)


def part1(ranges, ids):
    fresh_ids = 0
    for i in ids:
        for min_value, max_val in ranges:
            if min_value <= i <= max_val:
                fresh_ids += 1
                break
    return fresh_ids


def part2(ranges):
    current_range = ranges[0]
    tot = 0
    for next_range in ranges[1:]:
        if next_range[0] > current_range[1]:
            tot += 1 + current_range[1] - current_range[0]
            current_range = next_range
        elif next_range[0] - 1 <= current_range[1] <= next_range[1]:
            current_range = (current_range[0], next_range[1])
    return tot + 1 + current_range[1] - current_range[0]


if __name__ == "__main__":
    print(part1(ranges, ids))
    print(part2(ranges))
