def read_input(filename):
    with open(filename) as file:
        input = file.read().strip().split("\n\n")
    return input


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]


def check_board_for_win(board, board_size=5):
    win_row = ["X" for a in range(board_size)]
    rotated_board = rotated(board)
    for bingo_board in [board, rotated_board]:
        if win_row in bingo_board:
            return True
    return False


def calc_board_sum(board):
    total = 0
    for row in board:
        for num in row:
            if num != "X":
                total += num
    return total


def part1(input):
    numbers_to_draw = [int(x) for x in input[0].split(",")]
    bingo_boards = [
        [[int(num_str) for num_str in row.split()] for row in board_str.split("\n")]
        for board_str in input[1:]
    ]

    board_size = len(bingo_boards[0])

    for times_drawn, drawn_num in enumerate(numbers_to_draw):
        for board_number, board in enumerate(bingo_boards):
            for i in range(board_size):
                for j in range(board_size):
                    if board[i][j] == drawn_num:
                        board[i][j] = "X"
            if check_board_for_win(board, board_size):
                print(f"BINGO on board number {board_number} with number {drawn_num} drawn. times_drawn={times_drawn}")
                board_sum = calc_board_sum(board)
                ans = board_sum * drawn_num
                return ans


def main():
    sample_input = read_input("sample_input.txt")
    input = read_input("input.txt")

    assert part1(sample_input) == 4512

    part1ans = part1(input)
    print("part1:", part1ans)

    # assert part2(sample_input) ==

    # part2ans = part2(input)
    # print("part2:", part2ans)


if __name__ == "__main__":
    main()
