DEBUG = True


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


def part2(depths):
    increase_count = 0

    DEBUG and print(sum([depths[0], depths[1], depths[2]]))
    for index in range(1, len(depths) - 2):  # 1 2... 1997
        currentWindowSum = sum([depths[index], depths[index + 1], depths[index + 2]])
        previousWindowSum = sum([depths[index - 1], depths[index], depths[index + 1]])
        if currentWindowSum > previousWindowSum:
            DEBUG and print(currentWindowSum, "increased")
            increase_count += 1
        else:
            DEBUG and print(currentWindowSum, "decreased")
    return increase_count


def main():
    sample = read_input("sample_input.txt")
    depths = read_input("input.txt")

    DEBUG and print("Part1 sample:")
    assert part1(sample) == 7

    part1ans = part1(depths)
    print("part1:", part1ans)

    DEBUG and print("Part2 sample:")
    assert part2(sample) == 5

    part2ans = part2(depths)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
