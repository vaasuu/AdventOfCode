def read_input(filename):
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
    return input


def part1(input):
    pass


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 26397

    part1ans = part1(input)
    print("part1:", part1ans)

    # assert part2(sample_input) == 

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
