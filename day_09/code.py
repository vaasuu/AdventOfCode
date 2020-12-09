def read_input(filename):
    with open(filename) as file:
        input = file.readlines()
        return input

def part1(preamble_length, input):
    index = int(preamble_length)
    for num in input[preamble_length:len(input)]:
        preamble = input[int(index)-int(preamble_length):(int(index))]
        index += 1
        response = check_value(preamble, num)        
        if response[0] == False:
            return(int(response[1]))

def check_value(preamble, sum_val):
    for num1 in preamble:
        for num2 in preamble:
            if int(num1) != int(num2):    
                if int(num1)+int(num2) == int(sum_val):
                    return True, sum_val
    return False, sum_val

def part2(input, invalid_number):
    
    for index in range(len(input)):
        num_list = []
        addition = 0
        
        for i in range(index,len(input)):
            num_list.append(input[i])
            addition += int(input[i])
            if addition > int(invalid_number):
                break
            if addition == int(invalid_number):
                min_max_sum = int(min(num_list))+int(max(num_list))
                return min_max_sum

if __name__ == "__main__":
    input = read_input("input.txt")
    preamble_length = 25

    part1 = part1(preamble_length, input)
    print("Part1:", part1)
    part2 = part2(input, part1)
    print("Part2", part2)