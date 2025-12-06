import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "in"

with open(filename) as file:
    data = file.readlines()


def part1(lines):
    lines = [line.split() for line in lines]
    operators = lines.pop()
    results = lines.pop(0)
    for line in lines:
        for idx, val in enumerate(line):
            results[idx] = str(eval(results[idx] + operators[idx] + val))
    return sum(int(i) for i in results)


def part2(lines):
    lines = [i.strip("\n") for i in lines]
    operators = lines.pop().split()
    C = len(lines[0])
    columns = ["".join(i).strip() for i in zip(*lines)]
    last_split = 0
    tot = 0
    current_operator = 0
    idx = 0
    for column in columns:
        is_separator = column == ""
        is_last_col = idx == C - 1
        if is_separator or is_last_col:
            end_idx = idx + 1 if is_last_col and not is_separator else idx
            tot += eval(operators[current_operator].join(columns[last_split:end_idx]))
            current_operator += 1
            last_split = idx + 1
        idx += 1
    return tot


if __name__ == "__main__":
    print(part1(data))
    print(part2(data))
