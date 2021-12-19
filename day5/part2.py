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

    # horizontal
    if i[0][0] == i[1][0]:

        b = min(i[0][1], i[1][1])
        c = max(i[0][1], i[1][1])

        while b <= c:

            key = (i[0][0], b)

            points[key] += 1

            b += 1

    # vertical
    elif i[0][1] == i[1][1]:

        b = min(i[0][0], i[1][0])
        c = max(i[0][0], i[1][0])

        while b <= c:

            key = (b, i[0][1])

            points[key] += 1

            b += 1

    # 2 diagonal cases

    # downward diagonal
    elif i[0][0] - i[1][0] == i[0][1] - i[1][1]:

        if i[0][0] <= i[1][0] and i[0][1] <= i[1][1]:
            lower = i[0]
            higher = i[1]
        else:
            lower = i[1]
            higher = i[0]

        b = lower[0]
        c = lower[1]
        d = higher[0]

        while b <= d:

            key = (b, c)

            points[key] += 1

            b += 1
            c += 1

    # upward diagonal
    elif abs(i[0][0] - i[1][0]) == abs(i[0][1] - i[1][1]):

        b = min(i[0][0], i[1][0])
        c = max(i[0][0], i[1][0])
        d = max(i[0][1], i[1][1])

        while b <= c:

            key = (b, d)

            points[key] += 1
        
            b += 1
            d -= 1

overlapping_points = 0

for i in points:
    if points[i] > 1:
        overlapping_points += 1

print("part2", overlapping_points)