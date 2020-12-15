from collections import defaultdict

def read_input(filename):
    with open(filename) as file:
        starting_numbers = [int(number) for number in file.read().split(',')]
    return starting_numbers

def get_n_th_number(starting_numbers, n):
    # turn_count = 0
    last_number_spoken = 0
    spoken_numbers = {}
    last_time_spoken = defaultdict(list)

    for i in range(n):
        if i < len(starting_numbers):
            number = starting_numbers[i]
            spoken_numbers[i] = number
            last_number_spoken = number
            last_time_spoken[number].append(i)
        else:    
            if len(last_time_spoken[last_number_spoken]) < 2:
                number = 0
                spoken_numbers[i] = number
                last_number_spoken = number
                last_time_spoken[number].append(i)
            else:
                number = last_time_spoken[last_number_spoken][-1]-last_time_spoken[last_number_spoken][-2]
                spoken_numbers[i] = number
                last_number_spoken = number
                last_time_spoken[number].append(i)

    # print(spoken_numbers)
    return last_number_spoken


if __name__ == "__main__":
    starting_numbers = read_input("input.txt")
    # starting_numbers = [int(number) for number in open("example_input.txt").readlines()[0].split(',')]
    part1 = get_n_th_number(starting_numbers, 2020)
    print("Part1", part1)
    part2 = get_n_th_number(starting_numbers, 30000000)
    print("Part2", part2)