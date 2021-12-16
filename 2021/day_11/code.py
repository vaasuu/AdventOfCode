def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_adjacent_location_indices(i, j, hight, width):
    adjacent_indices = []
    # ones that share boundry
    if i > 0:
        adjacent_indices.append((i - 1, j)) # N
    if i + 1 < hight:
        adjacent_indices.append((i + 1, j)) # S
    if j > 0:
        adjacent_indices.append((i, j - 1)) # W
    if j + 1 < width:
        adjacent_indices.append((i, j + 1)) # E
    # diagonals
    if i > 0:
        adjacent_indices.append((i - 1, j - 1)) # NW
    if i + 1 < hight:
        adjacent_indices.append((i + 1, j + 1)) # SE
    if j > 0:
        adjacent_indices.append((i + 1, j - 1)) # SW
    if j + 1 < width:
        adjacent_indices.append((i - 1, j + 1)) # NE
    return adjacent_indices


def part1(lines):
    matrix = [list(map(int, line)) for line in lines]


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 1656

    part1ans = part1(lines)
    print("part1:", part1ans)

    # assert part2(sample_lines) ==

    # part2ans = part2(lines)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
