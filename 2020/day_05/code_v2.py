def read_input(filename):
    with open(filename) as file:
        boarding_passes = file.readlines()
        return boarding_passes

def get_seat_id(boarding_pass):
    seat_id = boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    seat_id = int(seat_id, base=2)
    return seat_id

def get_seat_id_list(boarding_passes):
    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]
    return seat_ids

def part1(seat_ids):
    return max(seat_ids)

def part2(seat_ids):
    missing_seats = sorted(set(range(min(seat_ids), max(seat_ids)+1)) - set(seat_ids))
    return missing_seats
    
if __name__ == "__main__":
    boarding_passes = read_input("input.txt")
    seat_ids = get_seat_id_list(boarding_passes)
    part1 = part1(seat_ids)
    part2 = part2(seat_ids)
    print("part1: ", part1)
    print("part2: ", part2)