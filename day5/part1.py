import re
from collections import defaultdict

with open('input.txt') as f:
    puzzle_input = f.read().split("\n")

puzzle_input = [re.split(' -> ', i) for i in puzzle_input]

# print(puzzle_input)

puzzle_input = list(map(lambda x: [i.split(",") for i in x], puzzle_input))

# print(puzzle_input)

puzzle_input = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y)), x)), puzzle_input))

# print(puzzle_input)

points = defaultdict(int)

for i in puzzle_input:

    # x1 equals x2
    if i[0][0] == i[1][0]:

        b = min(i[0][1], i[1][1])
        c = max(i[0][1], i[1][1])

        while b <= c:

            key = (i[0][0], b)

            points[key] += 1

            b += 1

    # y1 equals y2
    elif i[0][1] == i[1][1]:

        b = min(i[0][0], i[1][0])
        c = max(i[0][0], i[1][0])

        while b <= c:

            key = (b, i[0][1])

            points[key] += 1

            b += 1

overlapping_points = 0

for i in points:
    if points[i] > 1:
        overlapping_points += 1

print("part1", overlapping_points)