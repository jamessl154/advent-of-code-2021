def increment_die(die_value):

    die_value += 1

    if die_value > 100:
        die_value = 1

    return die_value

def move(board_index, total_die_value):

    result_move = total_die_value % 10

    new_index = board_index + result_move

    if new_index > 9:
        new_index -= 10

    return new_index

def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 1-10, 1-10 ...

    p1_count = 0
    p2_count = 0
    die_value = 0 # 1-100 circular like board
    die_rolls = 0

    # test input:
    # player 1 starts at 4 which is index 3 of board
    # player 2 starts at 8 which is index 7 of board

    # puzzle input:
    # player 1 starts at 6 which is index 5 of board
    # player 2 starts at 4 which is index 3 of board

    p1_board_index = 5
    p2_board_index = 3

    while True:

        # p1 turn
        die_rolls += 3

        p1_total_die_value = 0

        for i in range(3):
            die_value = increment_die(die_value)
            p1_total_die_value += die_value

        p1_board_index = move(p1_board_index, p1_total_die_value)
        p1_count += board[p1_board_index]

        if p1_count >= 1000:
            print("part1", die_rolls * p2_count)
            return

        # p2 turn
        die_rolls += 3

        p2_total_die_value = 0

        for i in range(3):
            die_value = increment_die(die_value)
            p2_total_die_value += die_value

        p2_board_index = move(p2_board_index, p2_total_die_value)
        p2_count += board[p2_board_index]

        if p2_count >= 1000:
            print("part1", die_rolls * p1_count)
            return

main()