def part1_count_trees(grid):
	numberoftrees = 0
	width_of_grid = len(grid[0])
	len_of_grid = len(grid)
	i = j = 0

	while j < len_of_grid:
		if grid[j][i] == '#':
			numberoftrees += 1
		j += 1
		i = (i+3)%width_of_grid

	return numberoftrees



def part2_multipleslopes(grid):
	productoftrees = 1
	width_of_grid = len(grid[0])
	len_of_grid = len(grid)

	for right, down in ((1,1), (3, 1), (5, 1), (7, 1), (1, 2)):
		i = j = 0
		numberoftrees = 0
		while j < len_of_grid:
			if grid[j][i] == '#':
				numberoftrees += 1
			j += down
			i = (i+right)%width_of_grid
		productoftrees *= numberoftrees
	return productoftrees


def read_input(filename):
	with open(filename) as file:
		input_values = [x.strip() for x in file.readlines()]

	return input_values

if __name__ == '__main__':
	input_values = ['..##.......',
				'#...#...#..',
				'.#....#..#.',
				'..#.#...#.#',
				'.#...##..#.',
				'..#.##.....',
				'.#.#.#....#',
				'.#........#',
				'#.##...#...',
				'#...##....#',
				'.#..#...#.#']
	input_values = read_input("input.txt")
	part1_ans = part1_count_trees(input_values)
	print("part1 answer: ", part1_ans)
	part2_ans = part2_multipleslopes(input_values)
	print("part2 answer: ", part2_ans)
