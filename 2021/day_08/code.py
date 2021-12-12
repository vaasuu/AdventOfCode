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


def part2(input):
    output_numbers = []

    for line in input:
        digit_sets_dict = {}
        list_235 = []
        list_069 = []

        unique_signal_patterns, output_values_string = line.split(" | ")
        for digit_str in unique_signal_patterns.split(" "):
            digit_length = len(digit_str)
            easy_digits = {2: 1, 4: 4, 3: 7, 7: 8}  # digit_segment_count:digit_int
            if digit_length in easy_digits.keys():
                digit = easy_digits[digit_length]
                digit_sets_dict[digit] = set(digit_str)
            elif digit_length == 5:
                list_235.append(set(digit_str))
            elif digit_length == 6:
                list_069.append(set(digit_str))

        for digit_set in list_235:
            if len(digit_set - digit_sets_dict[1]) == 3:
                digit_sets_dict[3] = digit_set
                list_235.remove(digit_set)
        for digit_set in list_235:
            if len(digit_set - digit_sets_dict[4]) == 3:
                digit_sets_dict[2] = digit_set
                list_235.remove(digit_set)
                digit_sets_dict[5] = list_235[0]
            else:
                digit_sets_dict[5] = digit_set
                list_235.remove(digit_set)
                digit_sets_dict[2] = list_235[0]

        for digit_set in list_069:
            if len(digit_set - digit_sets_dict[1]) == 5:
                digit_sets_dict[6] = digit_set
                list_069.remove(digit_set)
        for digit_set in list_069:
            if len(digit_set - digit_sets_dict[4]) == 3:
                digit_sets_dict[0] = digit_set
                list_069.remove(digit_set)
                digit_sets_dict[9] = list_069[0]
            else:
                digit_sets_dict[9] = digit_set
                list_069.remove(digit_set)
                digit_sets_dict[0] = list_069[0]

        # invert dict so key is sorted segment letters and value is integer
        ivd = {"".join(sorted(v)): k for k, v in digit_sets_dict.items()}
        output_digits_int_list = [
            ivd["".join(sorted(digit_str))]
            for digit_str in output_values_string.split(" ")
        ]
        output_digits_str_list = [str(i) for i in output_digits_int_list]
        output_digits_str = "".join(output_digits_str_list)
        output_number = int(output_digits_str)
        output_numbers.append(output_number)
    ans = sum(output_numbers)
    return ans


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 26

    part1ans = part1(input)
    print("part1:", part1ans)

    assert part2(sample_input) == 61229

    part2ans = part2(input)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
