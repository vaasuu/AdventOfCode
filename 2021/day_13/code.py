import numpy as np


def read_input(filename):
    with open(filename) as file:
        paper = file.read().strip()
    return paper


def parse_input(paper):
    coordinates_str, instructions_str = paper.split("\n\n")
    coordinates_str = [
        tuple(coordinate.split(",")) for coordinate in coordinates_str.splitlines()
    ]
    coordinates = [(int(x), int(y)) for x, y in coordinates_str]

    instructions = []
    for instruction in instructions_str.splitlines():
        axis, line = instruction.split("=")
        axis = axis[-1]
        line = int(line)
        instructions.append((axis, line))

    return coordinates, instructions


def part1(paper):
    coordinates, instructions = parse_input(paper)
    width = max(x for x, y in coordinates) + 1
    hight = max(y for x, y in coordinates) + 1
    matrix = np.zeros((hight, width), dtype=int)
    for x, y in coordinates:
        matrix[y][x] = 1
    print_np_array(matrix)

    for axis, line in instructions:
        if axis == "y":
            matrix = np.delete(matrix, line, 0)
            old, new = np.split(matrix, 2, 0)
            new_flipped = np.flip(new, 0)
        else:
            matrix = np.delete(matrix, line, 1)
            old, new = np.split(matrix, 2, 1)
            new_flipped = np.flip(new, 1)

        matrix = np.bitwise_or(old, new_flipped)
        print_np_array(matrix)

        ans = np.sum(matrix)
        return ans


def print_np_array(matrix):
    hight, width = matrix.shape
    for i in range(hight):
        line = ""
        for j in range(width):
            if matrix[i][j] == 1:
                line += "\u2588"
            else:
                line += "."
        print(line, end="\n")
    print("\n" * 2)


def part2(paper):
    coordinates, instructions = parse_input(paper)

    max_x = max(a[0] for a in coordinates)
    min_x = min(a[0] for a in coordinates)
    max_y = max(a[1] for a in coordinates)
    min_y = min(a[1] for a in coordinates)
    width = max_x + 1
    hight = max_y + 1

    matrix = np.zeros((hight, width), dtype=int)
    for x, y in coordinates:
        matrix[y][x] = 1
    print_np_array(matrix)

    matrix = matrix[min_y:]
    for axis, line in instructions:
        hight, width = matrix.shape
        if axis == "y":
            if hight % 2 != 0:
                matrix = np.delete(matrix, line, 0)
            old, new = np.split(matrix, 2, 0)
            new_flipped = np.flip(new, 0)
        else:
            matrix = np.delete(matrix, line, 1)
            old, new = np.split(matrix, 2, 1)
            new_flipped = np.flip(new, 1)

        matrix = np.bitwise_or(old, new_flipped)
        print_np_array(matrix)

    print_np_array(matrix)
    return 16


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 17

    part1ans = part1(lines)
    print("part1:", part1ans)

    assert part2(sample_lines) == 16

    part2ans = part2(lines)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
