def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_adjacent_location_indices(i, j, hight, width):
    adjacent_indices = []
    # ones that share boundry
    if i > 0:
        adjacent_indices.append((i - 1, j)) # N
    if i + 1 < hight:
        adjacent_indices.append((i + 1, j)) # S
    if j > 0:
        adjacent_indices.append((i, j - 1)) # W
    if j + 1 < width:
        adjacent_indices.append((i, j + 1)) # E
    # diagonals
    if i > 0:
        adjacent_indices.append((i - 1, j - 1)) # NW
    if i + 1 < hight:
        adjacent_indices.append((i + 1, j + 1)) # SE
    if j > 0:
        adjacent_indices.append((i + 1, j - 1)) # SW
    if j + 1 < width:
        adjacent_indices.append((i - 1, j + 1)) # NE
    return adjacent_indices


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n")


def step_forward(matrix, n):
    width = len(matrix[0])
    height = len(matrix)

    has_flashed = set()
    print_matrix(matrix)

    def flash_adjacent(i, j, height, width):
        adjacent_indices = set(
            get_adjacent_location_indices(i, j, height, width)
        )
        for adj_i, adj_j in adjacent_indices:
            matrix[adj_i][adj_j] += 1
            if matrix[adj_i][adj_j] > 9 and (adj_i, adj_j) not in has_flashed:
                has_flashed.add((adj_i, adj_j))
                print_matrix(matrix)
                flash_adjacent(adj_i, adj_j, height, width)
        return 


    for i in range(height):
        for j in range(width):
            matrix[i][j] += 1
    print_matrix(matrix)

    for i in range(height):
        for j in range(width):
            if matrix[i][j] > 9:
                has_flashed.add((i, j))
                print_matrix(matrix)
                flash_adjacent(i, j, height, width)

    for i in range(height):
        for j in range(width):
            if matrix[i][j] in has_flashed:
                matrix[i][j] = 0
    
    print_matrix(matrix)
    print("end")


def part1(lines):
    matrix = [list(map(int, line)) for line in lines]
    step_forward(matrix, n=1)

def main():
    sample_lines = read_input("sample_input.txt")
    lines = read_input("input.txt")

    assert part1(sample_lines) == 1656

    part1ans = part1(lines)
    print("part1:", part1ans)

    # assert part2(sample_lines) ==

    # part2ans = part2(lines)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
