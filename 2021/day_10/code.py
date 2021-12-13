from collections import deque


def read_input(filename):
    with open(filename) as file:
        input = [line.strip() for line in file.readlines()]
    return input


char_groups = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]
start_chars = [char for (char, _) in char_groups]
end_chars = [char for (_, char) in char_groups]
char_pairs = {
    **{start: end for (start, end) in char_groups},
    **{end: start for (start, end) in char_groups},
}  # merge two dicts together https://stackoverflow.com/a/26853961


def check_line(line):
    char_stack = deque()
    for char in line:
        if char in start_chars:
            char_stack.append(char)
        else:
            start_char = char_stack.pop()
            if char_pairs[start_char] != char:
                return ("corrupt", char)
    return ("valid", None)


def part1(input):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    scores = []

    for line in input:
        state, char = check_line(line)
        if state == "corrupt":
            scores.append(score_table[char])

    ans = sum(scores)
    return ans


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 26397

    part1ans = part1(input)
    print("part1:", part1ans)

    # assert part2(sample_input) ==

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
