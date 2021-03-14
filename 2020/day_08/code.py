def read_input(filename):
    with open(filename) as file:
        instructions = [line.strip() for line in file.readlines()]
    return instructions

#Part 1
def resolve(instructions):
    accumulation = 0
    visited = set()
    index = 0
    while index < len(instructions):
        if index in visited:
            return False, accumulation
        visited.add(index)
        instruction, num = instructions[index].split()
        if instruction == 'nop':
            index += 1
            continue
        elif instruction == 'jmp':
            index += int(num)
        elif instruction == 'acc':
            index += 1
            accumulation += int(num)
    return True, accumulation
        
def part1(instructions):
    return resolve(instructions)[1]

def part2(instructions):
    for i, line in enumerate(instructions):
        tokens = line.split()
        fixed = []
        if tokens[0] == "nop":
            fixed = instructions[:i] + ["jmp " + tokens[1]] + instructions[i+1:]
        elif tokens[0] == "jmp":
            fixed = instructions[:i] + ["nop " + tokens[1]] + instructions[i+1:]
        if fixed != []:
            resolved = resolve(fixed)
            if resolved[0]:
                return resolved[1]


if __name__ == "__main__":
    instructions = read_input("input.txt")
    part1 = part1(instructions)
    part2 = part2(instructions)
    print("Part1:", part1)
    print("Part2:", part2)