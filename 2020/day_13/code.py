def get_input(filename):
    with open(filename) as file:
        notes = file.readlines()
    return notes


def part1(notes):

    timestamp = int(notes[0])
    bus_ids = set(notes[1].split(','))
    bus_ids.discard('x') # remove x from bus_ids

    # for bus_id in bus_ids:
    #     time = timestamp
    #     increment = int(bus_id)

    #     while (time % increment) != 0:
    #         time += 1
    #     print("BusID", bus_id,"timestamp", time)

    time = timestamp
    waiting = True
    while waiting:
        for bus_id in bus_ids:
            mod = time % int(bus_id)
            if (mod) == 0:
                waiting = False
                print("BusID", bus_id,"timestamp", time)
                wait_time = time-timestamp
                return wait_time * int(bus_id)        
        time += 1
    
def part2(notes):
    bus_ids = notes[1].split(',')

    bus_ids = [(int(bus_id), i) for i, bus_id in enumerate(bus_ids) if bus_id != 'x']

    loops = 0 # For debugging
    jump = i = bus_ids[0][0]
    for bus_id in bus_ids[1:]:
        while (i+bus_id[1]) % bus_id[0] != 0:
            i += jump
            loops += 1 # For debugging only
        jump *= bus_id[0]
    return i


if __name__ == "__main__":
    notes = get_input("input.txt")
    # notes = get_input("sample_input.txt")
    # notes = get_input("test_input.txt")
    part1 = part1(notes)
    print("Part1:", part1)
    part2 = part2(notes)
    print("Part2:", part2)

