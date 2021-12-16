def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_adjacent_location_indices(i, j, height, width):
    adjacent_indices = []
    # ones that share boundry
    if i > 0:
        adjacent_indices.append((i - 1, j))  # N
    if i + 1 < height:
        adjacent_indices.append((i + 1, j))  # S
    if j > 0:
        adjacent_indices.append((i, j - 1))  # W
    if j + 1 < width:
        adjacent_indices.append((i, j + 1))  # E
    # diagonals
    if i > 0 and j > 0:
        adjacent_indices.append((i - 1, j - 1))  # NW
    if i < height - 1 and j < width - 1:
        adjacent_indices.append((i + 1, j + 1))  # SE
    if j > 0 and i + 1 < height:
        adjacent_indices.append((i + 1, j - 1))  # SW
    if j + 1 < width and i > 0:
        adjacent_indices.append((i - 1, j + 1))  # NE
    return adjacent_indices


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = " ".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))
    print("\n")


def step_forward(matrix, steps=1):
    width = len(matrix[0])
    height = len(matrix)

    total_flashes = 0

    for step in range(steps):

        flash_count = 0
        flashed = set()

        # increment all energy levels by 1
        for i in range(height):
            for j in range(width):
                matrix[i][j] += 1

        while True:
            prev_flash_count = flash_count

            for i in range(height):
                for j in range(width):
                    # flash octopi that are over 9 energy and have not been flashed before in this step
                    if matrix[i][j] > 9 and (i, j) not in flashed:
                        # flash the octopi
                        flashed.add((i, j))
                        for adj_i, adj_j in get_adjacent_location_indices(
                            i, j, height, width
                        ):
                            matrix[adj_i][adj_j] += 1
                        flash_count += 1

            if prev_flash_count == flash_count:
                break
        total_flashes += flash_count

        # reset octopi that are over 9 to 0
        for i in range(height):
            for j in range(width):
                if matrix[i][j] > 9:
                    matrix[i][j] = 0
        print(f"After step {step+1}")
        print_matrix(matrix)
        print(f"total_flashes: {total_flashes}")

    return total_flashes


def part1(lines):
    matrix = [list(map(int, line)) for line in lines]
    total_flashes = step_forward(matrix, steps=100)
    return total_flashes


def part2(lines):
    steps = 10000

    matrix = [list(map(int, line)) for line in lines]

    width = len(matrix[0])
    height = len(matrix)

    total_flashes = 0

    for step in range(steps):

        flash_count = 0
        flashed = set()

        # increment all energy levels by 1
        for i in range(height):
            for j in range(width):
                matrix[i][j] += 1

        while True:
            prev_flash_count = flash_count

            for i in range(height):
                for j in range(width):
                    # flash octopi that are over 9 energy and have not been flashed before in this step
                    if matrix[i][j] > 9 and (i, j) not in flashed:
                        # flash the octopi
                        flashed.add((i, j))
                        for adj_i, adj_j in get_adjacent_location_indices(
                            i, j, height, width
                        ):
                            matrix[adj_i][adj_j] += 1
                        flash_count += 1

            if prev_flash_count == flash_count:
                break
        total_flashes += flash_count

        # reset octopi that are over 9 to 0
        for i in range(height):
            for j in range(width):
                if matrix[i][j] > 9:
                    matrix[i][j] = 0
        print(f"After step {step+1}")
        print_matrix(matrix)
        zero_matrix = [([0] * 10) for i in range(10)]
        if matrix == zero_matrix:
            return step + 1


def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 1656

    part1ans = part1(lines)
    print("part1:", part1ans)

    assert part2(sample_lines) == 195

    part2ans = part2(lines)
    print("part2:", part2ans)


if __name__ == "__main__":
    main()
