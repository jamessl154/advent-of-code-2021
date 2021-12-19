with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

puzzle_input = list(map(lambda x: int(x), puzzle_input))

increased = 0

for i in range(1, len(puzzle_input)):
    if puzzle_input[i] > puzzle_input[i - 1]:
        increased += 1

print("part1", increased)

windows = 0

for i in range(2, len(puzzle_input) - 1):
    j = i - 1
    prev_window = puzzle_input[j - 1] + puzzle_input[j] + puzzle_input[j + 1]
    current_window = puzzle_input[i - 1] + puzzle_input[i] + puzzle_input[i + 1]
    if current_window > prev_window:
        windows += 1

print("part2", windows)