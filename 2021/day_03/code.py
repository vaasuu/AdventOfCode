import numpy as np
from copy import deepcopy


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def part1(lines):
    width = len(lines[0])
    a = [list(map(int, line)) for line in lines]
    array = np.array(a)
    columns = [array[:, col] for col in range(width)]
    most_common_bits = [np.bincount(col).argmax() for col in columns]
    c = map(str, most_common_bits)
    gamma_str = "".join(c)
    gamma = int(gamma_str, 2)
    epsilon_str = "".join("1" if x == "0" else "0" for x in gamma_str)
    epsilon = int(epsilon_str, 2)
    ans = gamma * epsilon
    return ans


def column(matrix, i):
    return [row[i] for row in matrix]


def average(lst):
    return sum(lst) / len(lst)


def which_to_keep(avg, return_val_if_equal):
    if avg < 0.5:
        most_common = 0
    elif avg > 0.5:
        most_common = 1
    else:
        return return_val_if_equal
    return most_common


def part2(lines):
    width = len(lines[0])
    a = [list(map(int, line)) for line in lines]

    columns = [column(a, col) for col in range(width)]
    column_averages = [average(col) for col in columns]
    keep_bits = [which_to_keep(col, 1) for col in column_averages]


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 198

    part1ans = part1(lines)
    print("part1:", part1ans)

    assert part2(sample_lines) == 230

    part2ans = part2(lines)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
