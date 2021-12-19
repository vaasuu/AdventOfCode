def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def part1(lines):
    matrix = [list(map(int, line)) for line in lines]
    width = len(matrix[0])
    height = len(matrix)


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 40

    part1ans = part1(lines)
    print("part1:", part1ans)

    # assert part2(sample_lines) ==

    # part2ans = part2(lines)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
