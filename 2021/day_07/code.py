def read_input(filename):
    with open(filename) as file:
        input = [int(num) for num in file.read().strip().split(",")]
    return input


def calculate_distances_to_value(target_val, list_of_values):
    distances = [abs(target_val - val) for val in list_of_values]
    return distances


def part1(input):
    #most_common_val = max(set(input), key=input.count)
    #distances = calculate_distances_to_value(most_common_val, input)

    fuelcosts = [sum(calculate_distances_to_value(i, input)) for i in range(1000)]

    ans = min(fuelcosts)
    return ans


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 37

    part1ans = part1(input)
    print("part1:", part1ans)

    # assert part2(sample_input) == 12

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
