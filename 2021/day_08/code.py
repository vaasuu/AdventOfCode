def read_input(filename):
    with open(filename) as file:
        input = [line for line in file.readlines()]
    return input


def part1(input):
    return ans


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 37

    part1ans = part1(input)
    print("part1:", part1ans)

    # assert part2(sample_input) == 168

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
