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

    if return_val_if_equal == 1:
        return most_common
    else:
        return int(not most_common)


def calc_keep_bits(a, return_val_if_equal):
    width = len(a[0])
    columns = [column(a, col) for col in range(width)]
    column_averages = [average(col) for col in columns]
    keep_bits = [which_to_keep(col, return_val_if_equal) for col in column_averages]
    return keep_bits


def calc_number_to_keep(a, return_val_if_equal):

    numbers_array = deepcopy(a)
    width = len(numbers_array[0])

    for col in range(width):
        keep_bits = calc_keep_bits(numbers_array, return_val_if_equal)
        for row in a:
            if row[col] != keep_bits[col]:
                try:
                    numbers_array.remove(row)
                except:
                    pass
            if len(numbers_array) == 1:
                num_str = "".join([str(x) for x in numbers_array[0]])
                num = int(num_str, 2)
                return num


def part2(lines):
    a = [list(map(int, line)) for line in lines]

    oxygen_generator_rating = calc_number_to_keep(a, 1)
    CO2_scrubber_rating = calc_number_to_keep(a, 0)
    ans = oxygen_generator_rating * CO2_scrubber_rating
    return ans


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
