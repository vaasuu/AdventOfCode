def read_input(filename):
    with open(filename) as file:
        input = [int(num) for num in file.read().strip().split(",")]
    return input


def calculate_fish(fish_states, days):
    fish_state_count = [0 for i in range(9)]

    for state in fish_states:
        fish_state_count[state] += 1

    for i in range(days):
        births = fish_state_count.pop(0)
        fish_state_count.append(births)
        fish_state_count[6] += births

    total_fish = sum(fish_state_count)
    return total_fish


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert calculate_fish(sample_input, 18) == 26
    assert calculate_fish(sample_input, 80) == 5934

    part1ans = calculate_fish(input, 80)
    print("part1:", part1ans)

    assert calculate_fish(sample_input, 256) == 26984457539

    part2ans = calculate_fish(input, 256)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
