from collections import Counter


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def step(template, rules, n):

    polymer = template

    for i in range(n):
        template_length = len(polymer)
        tmp_polymer = ""
        for templete_letter_index in range(template_length - 1):
            first_letter = polymer[templete_letter_index]
            second_letter = polymer[templete_letter_index + 1]
            letter_to_insert = rules[first_letter + second_letter]

            tmp_polymer += first_letter + letter_to_insert
            if templete_letter_index == template_length - 2:
                tmp_polymer += second_letter
        polymer = tmp_polymer
        print(f"After step {i+1}. Polymer length: {len(polymer)}")
    return polymer


def part1(lines):
    polymer_template = lines[0]
    pair_insertion_rules = lines[2:]

    rules = {}
    for rule in pair_insertion_rules:
        between_letters, letter_to_insert = rule.split(" -> ")
        rules[between_letters] = letter_to_insert

    polymer = step(polymer_template, rules, 10)
    counts = Counter(polymer)
    sorted_letter_frequency = sorted(counts.values())
    most_common = sorted_letter_frequency[-1]
    least_common = sorted_letter_frequency[0]
    ans = most_common - least_common
    return ans


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 1588

    part1ans = part1(lines)
    print("part1:", part1ans)

    # assert part2(sample_lines) ==

    # part2ans = part2(lines)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
