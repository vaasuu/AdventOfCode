def read_input(filename):
    with open(filename) as file:
        lines = file.read().strip()
    return lines


def part1(lines):
    pass

def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 1588

    part1ans = part1(lines)
    print("part1:", part1ans)

    # assert part2(sample_lines) ==

    # part2ans = part2(lines)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
