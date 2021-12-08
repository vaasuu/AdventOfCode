DEBUG = False

def read_input(filename):
    with open(filename) as file:
        input = [int(num) for num in file.read().strip().split(',')]
    return input

def list_to_str(lst):
    lst_str = ', '.join(map(str,lst))
    return lst_str

def part1(timers, days):
    DEBUG and print(f"Initial state: \t{list_to_str(timers)}")
    for i in range(days):
        for index in range(len(timers)):
            timers[index] -= 1
            if (timers[index] < 0):
                timers[index] = 6
                timers.append(8) # The new lanternfish starts with an 
                                     # internal timer of 8 and does not 
                                     # start counting down until the next day
                                     # 8+1 = 9
        DEBUG and print(f"After \t{i+1}\t days: {list_to_str(timers)}")
    total_fish = len(timers)
    print(f"After {days} days, there are {total_fish} fish")
    return total_fish


def part2(timers, days):
    DEBUG and print(f"Initial state: \t{list_to_str(timers)}")
    for i in range(days):
        for index in range(len(timers)):
            timers[index] -= 1
            if (timers[index] < 0):
                timers[index] = 6
                timers.append(8) # The new lanternfish starts with an 
                                     # internal timer of 8 and does not 
                                     # start counting down until the next day
                                     # 8+1 = 9
        DEBUG and print(f"After \t{i+1}\t days: {list_to_str(timers)}")
    total_fish = len(timers)
    print(f"After {days} days, there are {total_fish} fish")
    return total_fish


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input, 18) == 26
    #assert part1(sample_input, 80) == 5934

    part1ans = part1(input, 80)
    print("part1:", part1ans)

    # assert part2(sample_input) == 12

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
