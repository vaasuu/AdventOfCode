def read_input(filename):
    with open(filename) as file:
        boarding_passes = file.readlines()
        return boarding_passes

def split_list(list):
    half = len(list)//2
    return list[:half], list[half:]

def get_seat_id(boarding_pass):
    row = list(range(128))
    
    if boarding_pass[0] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]
    if boarding_pass[1] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]            
    if boarding_pass[2] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]            
    if boarding_pass[3] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]            
    if boarding_pass[4] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]            
    if boarding_pass[5] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]            
    if boarding_pass[6] == 'F':
        row = split_list(row)[0]
    else:
        row = split_list(row)[1]            

    seat = list(range(8))  
     
    if boarding_pass[7] == 'L':
        seat = split_list(seat)[0]
    else:
        seat = split_list(seat)[1]
    if boarding_pass[8] == 'L':
        seat = split_list(seat)[0]
    else:
        seat = split_list(seat)[1]
    if boarding_pass[9] == 'L':
        seat = split_list(seat)[0]
    else:
        seat = split_list(seat)[1]
    
    seat_id = row[0] * 8 + seat[0]
    return seat_id

def get_seat_id_list(boarding_passes):
    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]
    return seat_ids

def part1(seat_ids):
    sorted_seat_ids = sorted(seat_ids,reverse=True)
    return sorted_seat_ids[0]

def part2(seat_ids):
    sorted_seat_ids = sorted(seat_ids)
    for i in range(sorted_seat_ids[0], sorted_seat_ids[len(sorted_seat_ids)-1]): 
        if i not in sorted_seat_ids:
            break
    return i

if __name__ == "__main__":
    #boarding_passes = read_input("sample_input.txt")
    boarding_passes = read_input("input.txt")
    seat_ids = get_seat_id_list(boarding_passes)
    #print("Seat ids: ", seat_ids)
    part1 = part1(seat_ids)
    part2 = part2(seat_ids)

    print("part1: ", part1)
    print("part2: ", part2)
