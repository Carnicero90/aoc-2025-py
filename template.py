import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils import timing

filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    pass


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
