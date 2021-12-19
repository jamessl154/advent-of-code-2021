with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

puzzle_input = list(map(lambda x: x.split(" "), puzzle_input))

depth = 0
horizontal = 0

for i in puzzle_input:
    if i[0] == "forward":
        horizontal += int(i[1])
    if i[0] == "down":
        depth += int(i[1])
    if i[0] == "up":
        depth -= int(i[1])

print("part1", horizontal * depth)

aim = 0
depth = 0
horizontal = 0

for i in puzzle_input:
    if i[0] == "forward":
        horizontal += int(i[1])
        depth += aim * int(i[1])
    if i[0] == "down":
        aim += int(i[1])
    if i[0] == "up":
        aim -= int(i[1])

print("part2", horizontal * depth)