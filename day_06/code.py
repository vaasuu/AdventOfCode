with open('input.txt') as file:
    groups = file.read().split('\n\n')

part1 = sum([len(set(group)) for group in [x.replace('\n', '') for x in groups]])
print("Part1:", part1)

part2 = sum([len(set.intersection(*[set(person) for person in group.split('\n')])) for group in groups])
print("Part2:", part2)