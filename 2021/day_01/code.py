DEBUG = False


def read_input(filename):
    with open(filename) as file:
        depths = [int(line.strip()) for line in file.readlines()]
    return depths


def part1(depths):
    increase_count = 0
    DEBUG and print(depths[0])

    for index in range(1, len(depths)):  # 1 2... 1999
        current = depths[index]
        previous = depths[index - 1]
        if current > previous:
            DEBUG and print(current, "increased")
            increase_count += 1
        else:
            DEBUG and print(current, "decreased")
    return increase_count


def main():
    part1_sample = read_input("sample_input.txt")
    depths = read_input("input.txt")

    DEBUG and print("Part1 sample:")
    assert part1(part1_sample) == 7

    part1ans = part1(depths)
    print("part1:", part1ans)


if __name__ == "__main__":
    main()
