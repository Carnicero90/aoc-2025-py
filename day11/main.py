import sys
from functools import lru_cache
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils import timing

filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    data = file.readlines()
    nodes = {}
    for line in data:
        node, next_nodes = line.strip().split(": ")
        nodes[node] = [i.strip() for i in next_nodes.split(" ")]


@lru_cache(maxsize=None)
def dfs1(current_node):
    if current_node == "out":
        return 1
    return sum(dfs1(next_node) for next_node in nodes[current_node])


@lru_cache(maxsize=None)
def dfs2(current_node, status):
    if current_node == "fft":
        status ^= 2
    if current_node == "dac":
        status ^= 1
    if current_node == "out":
        return status == 3
    return sum(dfs2(next_node, status) for next_node in nodes[current_node])


@timing()
def part1():
    return dfs1("you")


@timing()
def part2():
    return dfs2("svr", 0)


if __name__ == "__main__":
    print(part1())
    print(part2())
