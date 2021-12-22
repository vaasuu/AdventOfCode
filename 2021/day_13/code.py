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
    print(coordinates)
    matrix = np.zeros((hight, width), dtype=int)
    for x, y in coordinates:
        matrix[y][x] = 1
    print(matrix, end="\n\n")

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
        print(matrix, end="\n\n")

        ans = np.sum(matrix)
        return ans


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 17

    part1ans = part1(lines)
    print("part1:", part1ans)

    # assert part2(sample_lines) ==

    # part2ans = part2(lines)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
