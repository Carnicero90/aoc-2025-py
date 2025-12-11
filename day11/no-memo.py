import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from utils import timing

# soluzione senza fare leva su lru_cache o memoization
filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    data = file.readlines()
    nodes = {}
    for line in data:
        node, next_nodes = line.strip().split(": ")
        nodes[node] = dict((i.strip(), 1) for i in next_nodes.split(" "))


def no_memo(start, end):
    total = 0
    queue = deque([(start, 1)])

    while queue:
        current_node, paths = queue.popleft()
        next_nodes = nodes[current_node].copy()
        for dr in next_nodes.items():
            node, routes = dr
            if node == end:
                total += paths * routes
                continue
            if node in {"out", "dac", "fft"}:
                continue
            else:
                queue.append((node, paths * routes))
                if (
                    "out" not in nodes[node]
                    and "dac" not in nodes[node]
                    and "fft" not in nodes[node]
                ):
                    for next_link in nodes[node].items():
                        nodes[current_node][next_link[0]] = (
                            nodes[current_node].get(next_link[0], 0)
                            + next_link[1] * nodes[current_node][node]
                        )
                    nodes[current_node].pop(node)
    return total


@timing()
def part1():
    return no_memo("you", "out")


@timing()
def part2():
    return no_memo("dac", "out") * no_memo("fft", "dac") * no_memo("svr", "fft")


if __name__ == "__main__":
    print(part1())
    print(part2())
