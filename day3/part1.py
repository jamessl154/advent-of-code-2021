from collections import defaultdict

with open("input.txt", "r") as f:
    puzzle_input = [i.strip() for i in f]

# print(puzzle_input)

tracker = defaultdict(int)

for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[i])):
        if puzzle_input[i][j] == "1":
            tracker[j] += 1

gamma = ''
epsilon = ''

for i in range(len(tracker)):
    if tracker[i] > len(puzzle_input) // 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# print(gamma, epsilon)
# print(int(gamma, 2), int(epsilon, 2))

print("part1", int(gamma, 2) * int(epsilon, 2))