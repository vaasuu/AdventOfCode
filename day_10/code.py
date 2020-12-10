with open("input.txt") as file:
    adapters = [int(line) for line in file]

# adapters = [int(line) for line in """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3""".splitlines()]

# part 1

adapters.append(max(adapters)+int(3))

jolt_rating = 0
count_1_jolt_diff = 0
count_3_jolt_diff = 0

for adapter in adapters:
    if jolt_rating+1 in adapters:
        jolt_rating += 1
        count_1_jolt_diff += 1
        print("Diff of 1")
    elif jolt_rating+2 in adapters:
        jolt_rating += 2
        print("Diff of 2")
    elif jolt_rating+3 in adapters:
        jolt_rating += 3
        count_3_jolt_diff += 1
        print("Diff of 3")
    else: 
        print("Adapter chain not possible.")

part1 = count_1_jolt_diff * count_3_jolt_diff
print("Part1:", part1)

# part 2

