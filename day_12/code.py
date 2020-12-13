import numpy as np

def get_input(filename):
    with open(filename) as file:
        instructions = [line.strip() for line in file.readlines()]
    return instructions

def part1(instructions):
    direction = 0
    coordinate = np.array([0,0])

    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        # print(action, value)
        if action == 'N':
            coordinate += np.array([0,value])
        elif action == 'S':
            coordinate += np.array([0,-value])
        elif action == 'E':
            coordinate += np.array([value,0])
        elif action == 'W':
            coordinate += np.array([-value,0])
        elif action == 'L':
            direction += value            
        elif action == 'R':
            direction -= value
        elif action == 'F':
            x = int(np.cos(direction*(2*np.pi/360))*value)
            y = int(np.sin(direction*(2*np.pi/360))*value)
            coordinate += np.array([x,y])
        # print(coordinate, direction)
    manhattan_distance = abs(coordinate[0])+abs(coordinate[1])
    return manhattan_distance

def part2(instructions):
    waypoint_coordinate_relative_to_ship = np.array([10,1])
    ship_current_coordinate = np.array([0,0])

    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        # print(action, value)
        if action == 'N':
            waypoint_coordinate_relative_to_ship += np.array([0,value])
        elif action == 'S':
            waypoint_coordinate_relative_to_ship += np.array([0,-value])
        elif action == 'E':
            waypoint_coordinate_relative_to_ship += np.array([value,0])
        elif action == 'W':
            waypoint_coordinate_relative_to_ship += np.array([-value,0])
        elif action == 'L':
            current_direction = np.arctan2(waypoint_coordinate_relative_to_ship[1], waypoint_coordinate_relative_to_ship[0])
            length = np.linalg.norm(waypoint_coordinate_relative_to_ship)
            x = round(np.cos(current_direction+value*(2*np.pi/360))*length)
            y = round(np.sin(current_direction+value*(2*np.pi/360))*length)
            waypoint_coordinate_relative_to_ship = np.array([x,y])

        elif action == 'R':
            current_direction = np.arctan2(waypoint_coordinate_relative_to_ship[1], waypoint_coordinate_relative_to_ship[0])
            length = np.linalg.norm(waypoint_coordinate_relative_to_ship)
            x = round(np.cos(current_direction-value*(2*np.pi/360))*length)
            y = round(np.sin(current_direction-value*(2*np.pi/360))*length)
            waypoint_coordinate_relative_to_ship = np.array([x,y])

        elif action == 'F':
            ship_current_coordinate += value*waypoint_coordinate_relative_to_ship
        
        # print("waypoint relative to ship",waypoint_coordinate_relative_to_ship)
        # print("waypoint current cords---",ship_current_coordinate+waypoint_coordinate_relative_to_ship)
        # print("ship current cords-------",ship_current_coordinate)   
    manhattan_distance = abs(ship_current_coordinate[0])+abs(ship_current_coordinate[1])
    return manhattan_distance



if __name__ == "__main__":
    # instructions = get_input("sample_input.txt")
    instructions = get_input("input.txt")
    part1 = part1(instructions)
    print("Part1:", part1)
    part2 = part2(instructions)
    print("Part2:", part2)
    
