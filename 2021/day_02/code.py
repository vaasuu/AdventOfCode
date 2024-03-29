def read_input(filename):
    with open(filename) as file:
        instructions = [line.strip() for line in file.readlines()]
    return instructions


def part1(instructions):
    x = 0
    y = 0

    for instruction in instructions:
        action, amount = instruction.split()
        amount = int(amount)

        if action == "forward":
            x += amount
        elif action == "down":
            y -= amount
        elif action == "up":
            y += amount
    ans = abs(x * y)
    return ans


def part2(instructions):
    x = 0
    y = 0
    aim = 0

    for instruction in instructions:
        action, amount = instruction.split()
        amount = int(amount)

        if action == "forward":
            x += amount
            y -= aim * amount
        elif action == "down":
            aim += amount
        elif action == "up":
            aim -= amount

    ans = abs(x * y)
    return ans


def main():
    sample_instructions = read_input("sample_input.txt")
    instructions = read_input("input.txt")

    assert part1(sample_instructions) == 150

    part1ans = part1(instructions)
    print("part1:", part1ans)

    assert part2(sample_instructions) == 900

    part2ans = part2(instructions)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
