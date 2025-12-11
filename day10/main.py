import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

filename = sys.argv[1] if len(sys.argv) > 1 else "in"


def min_steps(start, masks, target):
    masks_n = [int(m, 2) for m in masks]
    max_steps = len(masks_n) - 1

    queue = deque([(int(start, 2), 0)])
    steps_to_state = dict()

    while queue:
        state, steps = queue.popleft()

        for m in masks_n:
            new_state = state ^ m
            new_steps = steps + 1
            if (
                new_state not in steps_to_state
                or new_steps < steps_to_state[new_state]
                and new_steps <= max_steps
            ):
                steps_to_state[new_state] = new_steps
                queue.append((new_state, new_steps))

    return steps_to_state[int(target, 2)]


with open(filename) as file:
    data = file.readlines()
    res = []
    ld = len(data)


def part1():
    tot = 0

    # ugly parsing
    for i in range(ld):
        target = data[i].split("]")[0][1:].replace(".", "0").replace("#", "1")

        raw_masks = eval(
            "[ " + data[i].split("]")[1].split("{")[0].replace(")", "),") + "]"
        )
        masks = []
        for x, el in enumerate(raw_masks):
            b = []
            for y in range(len(target)):
                if type(el) is int:
                    el = tuple([el])
                b.append("1" if y in el else "0")
            masks.append("".join(b))

        initial_status = "0" * len(target)

        tot += min_steps(initial_status, masks, target) or 0
    return tot


def part2():
    return "non sono capace"


if __name__ == "__main__":
    print(part1())
    print(part2())
