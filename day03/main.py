import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    batteries = file.readlines()


def max_battery_value(battery, max_digits=2):
    battery_len = len(battery)
    current_block = [*battery[:max_digits]]

    for start_pos in range(1, battery_len - 1):
        candidate = battery[start_pos : min(start_pos + max_digits, battery_len - 1)]

        for i in range(0, len(candidate)):
            if current_block[i] < candidate[i]:
                start_idx = i + max_digits - len(candidate)
                current_block[start_idx:] = candidate[i:]
                break
    return int("".join(current_block))


def part1():
    return sum(max_battery_value(b, 2) for b in batteries)


def part2():
    return sum(max_battery_value(b, 12) for b in batteries)


if __name__ == "__main__":
    print(part1())
    print(part2())
