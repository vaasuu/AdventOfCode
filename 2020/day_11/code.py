from copy import deepcopy

def get_input(filename):
    with open(filename) as file:
        seats = [list(line.strip()) for line in file.readlines()]
        # print(seats)
    return seats

def get_seat_value(seats,i,j):
    try:
        if 0 <= i < len(seats) and 0 <= j < len(seats[0]):
            value = seats[i][j]
            return value
    except IndexError:
        pass

def count_surrouding_chairs(seats,i,j):
    floor_count = 0
    empty_count = 0
    occupied_count = 0

    for row, column in list([[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]):
        value = get_seat_value(seats,int(i+row),int(j+column))
        if value == 'L':
            empty_count += 1
        elif value == '.':
            floor_count += 1
        elif value == '#':
            occupied_count += 1

    return floor_count, empty_count, occupied_count


def print_seat_map(seats):
    for line in seats:
        print(*line)

# def change_seats(seats):
#     changed = False
#     seat_copy = deepcopy(seats)
#     for i in range(len(seats)):
#         for j in range(len(seats[0])):
#             seat_value = get_seat_value(seats,i,j)
#             occupied_count = count_surrouding_chairs(seats,i,j)[2]
            
#             if seat_value == 'L' and occupied_count == 0:
#                 seat_copy[i][j] = '#'
#                 changed = True
#             elif seat_value == '#' and occupied_count >= 4:
#                 seat_copy[i][j] = 'L'
#                 changed = True
#             else: 
#                 seat_copy[i][j] = seats[i][j]

#     return seat_copy, changed

def part1(seats):
    seat_copy = deepcopy(seats)
    while True:    
        changed = False
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                seat_value = get_seat_value(seats,i,j)
                occupied_count = count_surrouding_chairs(seats,i,j)[2]
                
                if seat_value == 'L' and occupied_count == 0:
                    seat_copy[i][j] = '#'
                    changed = True
                elif seat_value == '#' and occupied_count >= 4:
                    seat_copy[i][j] = 'L'
                    changed = True
        seats = deepcopy(seat_copy)

        if not changed:
            break
    # print_seat_map(seat_copy)
    return str(seat_copy).count('#')


# Part2

def count_visible_chairs(seats,i,j):
    floor_count = 0
    empty_count = 0
    occupied_count = 0

    for row, column in list([[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]):
        distance = 0
        while True:
            distance += 1
            value = get_seat_value(seats,int(i+distance*row),int(j+distance*column))
            if value == 'L':
                empty_count += 1
                break
            elif value == '#':
                occupied_count += 1
                break
            elif value == None:
                break  
    return floor_count, empty_count, occupied_count



def part2(seats):
    seat_copy = deepcopy(seats)
    while True:    
        changed = False
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                seat_value = get_seat_value(seats,i,j)
                occupied_count = count_visible_chairs(seats,i,j)[2]
                
                if seat_value == 'L' and occupied_count == 0:
                    seat_copy[i][j] = '#'
                    changed = True
                elif seat_value == '#' and occupied_count >= 5:
                    seat_copy[i][j] = 'L'
                    changed = True
        seats = deepcopy(seat_copy)

        if not changed:
            break
    # print_seat_map(seat_copy)
    return str(seat_copy).count('#')


if __name__ == "__main__":
    seats = get_input("input.txt")
    # seats = get_input("sample_input.txt")
    part1 = part1(seats)
    print("Part1:", part1)

    part2 = part2(seats)
    print("Part2:", part2)
