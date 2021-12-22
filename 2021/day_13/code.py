def read_input(filename):
    with open(filename) as file:
        paper = file.read().strip()
    return paper


def parse_input(paper):
    coordinates_str, instructions_str = paper.split("\n\n")
    coordinates_str = [
        tuple(coordinate.split(",")) for coordinate in coordinates_str.splitlines()
    ]
    coordinates = set((int(x), int(y)) for x, y in coordinates_str)

    instructions = []
    for instruction in instructions_str.splitlines():
        axis, line = instruction.split("=")
        axis = axis[-1]
        line = int(line)
        instructions.append((axis, line))

    return coordinates, instructions


def folding(paper, stop_on_first_fold):
    coordinates, instructions = parse_input(paper)
    print_grid(coordinates)
    for axis, line in instructions:
        if axis == "y":
            coordinates = {(x, y if y < line else 2 * line - y) for x, y in coordinates}
        else:
            coordinates = {(x if x < line else 2 * line - x, y) for x, y in coordinates}

        print_grid(coordinates)

        if stop_on_first_fold:
            ans = len(coordinates)
            return ans

    return len(coordinates)


def print_grid(coordinates):
    width = max(x for x, y in coordinates)
    hight = max(y for x, y in coordinates)

    for y in range(hight + 1):
        line = ""
        for x in range(width + 1):
            if (x, y) in coordinates:
                line += "\u2588"
            else:
                line += "."
        print(line, end="\n")
    print("\n" * 2)


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    # part1
    assert folding(sample_lines, True) == 17

    part1ans = folding(lines, True)
    print("part1:", part1ans)

    # part2
    assert folding(sample_lines, False) == 16

    part2ans = folding(lines, False)
    print("part2: Look at text ^")


if __name__ == "__main__":
    main()
