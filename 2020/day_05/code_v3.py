with open("input.txt") as file:
    seat_ids = [int(boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'),2) for boarding_pass in file]
    print("part1: ", max(seat_ids))
    print("part2: ", set(range(min(seat_ids), max(seat_ids))) - set(seat_ids))
