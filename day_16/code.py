import re

def get_input(filename):
    with open(filename) as file:
        input_text = file.read()
        return input_text

def part1(input_text):

    not_valid = []
    valid = []

    input_text = input_text.split('\n\n')
    rule_lines = input_text[0].splitlines()
    # print(rule_lines)

    nearby_tickets = [int(val) for sublist in [line.split(',') for line in input_text[2].splitlines()[1:]] for val in sublist]
    # print(nearby_tickets)

    for number in nearby_tickets:
        valid_counter = 0
        for rule_line in rule_lines:

                # print(rule)
                regex = re.search(r'(\d+)-(\d+) or (\d+)-(\d+)', rule_line)
                
                # print(regex.group(1,2,3,4))
                min_value1, max_value1, min_value2, max_value2 = regex.group(1,2,3,4)
                if int(min_value1) <= number <= int(max_value1) or int(min_value2) <= number <= int(max_value2):
                    valid_counter += 1
                else:
                    pass            
        if valid_counter == 0:
            not_valid.append(number)
        else:
            valid.append(number)

                
    print("Not valid:", not_valid)
    
    return sum(not_valid)


if __name__ == "__main__":
    input_text = get_input("input.txt")
    # input_text = get_input("sample_input_part1.txt")
    part1 = part1(input_text)
    print("Part1:", part1)
    