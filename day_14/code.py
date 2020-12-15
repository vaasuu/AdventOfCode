import re

def read_input(filename):
    with open(filename) as file:
        input_data = [line.strip() for line in file.readlines()]
    return input_data

# Part1

def part1(input):
    memory = {}

    for line in input:
        mask_match = re.search(r'mask = (.*)', line)
        if mask_match != None:
            mask = mask_match.group(1)
        else:
            match = re.search(r'mem\[(.*)\] = (.*)', line)
            address = int(match.group(1))
            value = list(format(int(match.group(2)), '036b'))

            for bit in range(len(mask)):
                if mask[bit] != 'X':
                    value[bit] = mask[bit] 
            
            memory[address] = value
    # print(memory)

    memory_sum = sum([int(''.join(binary_number), 2) for binary_number in list(memory.values())])
    return memory_sum

# Part2

def get_combinations(address, floating_bits):
    binary_numbers = []
    for i in range(2**len(floating_bits)):
        binary_num = format(i, '0'+str(len(floating_bits))+'b')
        binary_numbers.append(binary_num)
    
    address_list = []
    for binary_num in binary_numbers:
        address_copy = address.copy()
        for floating_bit_index, new_bit_value in enumerate(list(binary_num)):
            address_copy[floating_bits[int(floating_bit_index)]] = new_bit_value
        address_list.append(address_copy)
        # print(''.join(address_copy))

    return address_list



def part2(input):
    memory = {}

    for line in input:
        mask_match = re.search(r'mask = (.*)', line)
        if mask_match != None:
            mask = mask_match.group(1)
        else:
            match = re.search(r'mem\[(.*)\] = (.*)', line)
            address = list(format(int(match.group(1)), '036b'))
            value = int(match.group(2))
            # print("orig",''.join(address))
            # print("mask", ''.join(mask))
            floating_bits = []
            for bit in range(len(mask)):
                if mask[bit] == '0':
                    pass 
                elif mask[bit] == '1':
                    address[bit] = '1'
                else:
                    address[bit] = 'X'
                    floating_bits.append(bit)

            # print("rslt",''.join(address))
            # print("------------")

            address_list = get_combinations(address, floating_bits)

            for k in address_list:
                address = int(''.join(k), 2)
                memory[address] = value                      
                        
    memory_sum = sum(list(memory.values()))
    return memory_sum


if __name__ == "__main__":
    # input_data = read_input("example_input1.txt")
    # input_data = read_input("example_input2.txt")
    input_data = read_input("input.txt")
    part1 = part1(input_data)
    print("Part1:", part1)
    part2 = part2(input_data)
    print("Part2:", part2)
