import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils import timing

filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    data = file.readlines()

start = data[0].index("S")
SPLT = "^"


@timing()
def part1():
    hits = set()
    paths = {start}
    for y in range(2, len(data), 2):
        line = data[y].strip()
        new_paths = set()
        for pos in paths:
            if line[pos] == SPLT:
                hits.add((pos, y))
                new_paths.add(pos - 1)
                new_paths.add(pos + 1)
            else:
                new_paths.add(pos)
        paths = new_paths
    return len(hits)


@timing()
def part2():
    paths = {start: 1}
    for y in range(2, len(data), 2):
        line = data[y].strip()
        new_paths = {}
        for pos, count in paths.items():
            if line[pos] == SPLT:
                left = pos - 1
                right = pos + 1
                new_paths[left] = new_paths.get(left, 0) + count
                new_paths[right] = new_paths.get(right, 0) + count
            else:
                new_paths[pos] = new_paths.get(pos, 0) + count
        paths = new_paths

    return sum(paths.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
