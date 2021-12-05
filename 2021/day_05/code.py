from collections import Counter
from collections import defaultdict


def read_input(filename):
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
    return input


def part1(input):
    cords = []

    for line in input:
        start, stop = line.split(" -> ")
        x1, y1 = [int(c) for c in start.split(",")]
        x2, y2 = [int(c) for c in stop.split(",")]
        if x1 == x2 or y1 == y2:
            if x1 < x2:
                x_cords = list(range(x1, x2 + 1))
            else:
                x_cords = list(range(x2, x1 + 1))
            for x_cord in x_cords:
                if y1 < y2:
                    y_cords = list(range(y1, y2 + 1))
                else:
                    y_cords = list(range(y2, y1 + 1))
                for y_cord in y_cords:
                    cords.append((x_cord, y_cord))
    # max_x = max([xytuple[0] for xytuple in cords])
    # max_y = max([xytuple[1] for xytuple in cords])
    # print(Counter(cords))
    total_points_overlapping = len([p for p in Counter(cords).values() if p >= 2])
    return total_points_overlapping


def print_map(cords):
    max_x = max([xytuple[0] for xytuple in cords])
    max_y = max([xytuple[1] for xytuple in cords])

    d = defaultdict(int, Counter(cords))

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(d[(x, y)], end="")
        print("\n", end="")


def part2(input):
    cords = []

    for line in input:
        start, stop = line.split(" -> ")
        x1, y1 = [int(c) for c in start.split(",")]
        x2, y2 = [int(c) for c in stop.split(",")]

        if x1 < x2:
            x_cords = list(range(x1, x2 + 1))
        else:
            x_cords = list(range(x2, x1 + 1))

        if x1 == x2:
            x_cord = x_cords[0]
            if y1 < y2:
                y_cords = list(range(y1, y2 + 1))
            else:
                y_cords = list(range(y2, y1 + 1))
            for y_cord in y_cords:
                cords.append((x_cord, y_cord))
        else:
            k = int((y1 - y2) / (x1 - x2))
            b = y1 - k * x1

            for x_cord in x_cords:
                y_cord = k * x_cord + b
                cords.append((x_cord, y_cord))
    # print_map(cords)
    # print(Counter(cords))
    total_points_overlapping = len([p for p in Counter(cords).values() if p >= 2])
    return total_points_overlapping


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 5

    part1ans = part1(input)
    print("part1:", part1ans)

    assert part2(sample_input) == 12

    part2ans = part2(input)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
