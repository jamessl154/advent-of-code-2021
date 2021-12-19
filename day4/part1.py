from collections import defaultdict

with open("input.txt", "r") as f:
    puzzle_input = f.read()

temp = puzzle_input.split("\n\n")

bingo_numbers = temp[0].split(",")

temp = list(map(lambda x: x.replace("  ", " ").split("\n"), temp))

bingo_boards = temp[1:]

bingo_boards = list(map(lambda x: list(map(lambda y: y.strip().split(" "), x)), bingo_boards))

# print(bingo_boards)

bingo_checker = []
for i in bingo_boards:
    row = defaultdict(int)
    col = defaultdict(int)
    bingo_checker.append([row, col])

def play_bingo():
    for i in bingo_numbers:
        for j in range(len(bingo_boards)):
            for k in range(len(bingo_boards[j])):
                for l in range(len(bingo_boards[j][k])):
                    if bingo_boards[j][k][l] == i:
                        bingo_checker[j][0][k] += 1
                        bingo_checker[j][1][l] += 1
                        if bingo_checker[j][0][k] == len(bingo_boards[0][0]) or bingo_checker[j][1][l] == len(bingo_boards[0]):
                            # first winning board
                            return (bingo_boards[j], (j, k, l))
                        bingo_boards[j][k][l] = True

first_winning_board, index_just_called = play_bingo()

# print(first_winning_board)
# print(index_just_called)

j, k, l = index_just_called

number_just_called = int(bingo_boards[j][k][l])

bingo_boards[j][k][l] = True

sum_unmarked = 0

for i in first_winning_board:
    for j in i:
        if j != True:
            sum_unmarked += int(j)

print("part1", sum_unmarked * number_just_called)