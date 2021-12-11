import numpy as np


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_adjacent_location_indices(i, j, matrix, hight, width):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < hight:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < width:
        adjacent_indices.append((i, j + 1))
    return adjacent_indices


def get_values_for_indices(indices, matrix):
    values = [matrix[i][j] for i, j in indices]
    return values


def get_low_points(matrix):
    low_points = []

    width = len(matrix[0])
    hight = len(matrix)
    for i in range(hight):
        for j in range(width):
            adjacent_indices = get_adjacent_location_indices(i, j, matrix, hight, width)
            adjacent_values = get_values_for_indices(adjacent_indices, matrix)
            current_cell_val = matrix[i][j]
            if current_cell_val < min(adjacent_values):
                low_points.append((i, j))
    return low_points


def part1(lines):
    matrix = [list(map(int, line)) for line in lines]
    low_points = get_low_points(matrix)
    low_point_values = [matrix[i][j] for i, j in low_points]
    ans = sum([val + 1 for val in low_point_values])
    return ans


def part2(lines):
    matrix = [list(map(int, line)) for line in lines]
    low_points = get_low_points(matrix)

    seen = set()

    def area(row, col):
        if not (
            0 <= row < len(matrix)
            and 0 <= col < len(matrix[0])
            and (row, col) not in seen
            and matrix[row][col] != 9
        ):
            return 0
        seen.add((row, col))
        return (
            1
            + area(row + 1, col)
            + area(row - 1, col)
            + area(row, col - 1)
            + area(row, col + 1)
        )

    areas = [area(row, col) for row, col in low_points]
    sorted_areas = sorted(areas, reverse=True)
    ans = sorted_areas[0] * sorted_areas[1] * sorted_areas[2]
    return ans


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 15

    part1ans = part1(lines)
    print("part1:", part1ans)

    assert part2(sample_lines) == 1134

    part2ans = part2(lines)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
