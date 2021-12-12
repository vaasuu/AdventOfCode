def read_input(filename):
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
    return input


def part1(input):
    found_digit_count = 0

    for line in input:
        unique_signal_patterns, output_values_string = line.split(" | ")
        for digit in output_values_string.split(" "):
            digit_length = len(digit)
            if digit_length in [
                2,
                4,
                3,
                7,
            ]:  # digit 1 uses 2 segments. 4 uses 4, 7 uses 3 and 8 uses 7
                found_digit_count += 1
    return found_digit_count


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 26

    part1ans = part1(input)
    print("part1:", part1ans)

    # assert part2(sample_input) == 61229

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
