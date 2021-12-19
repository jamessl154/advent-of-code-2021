from collections import defaultdict
from heapq import heappush, heappop

puzzle_input = [x for x in open("part2.txt").read().splitlines()]

# Some help from: https://github.com/mebeim/aoc/blob/master/2021/README.md#day-15---chiton

def adj_squares(grid, i, j):

    neighbours = []

    height = len(grid)
    width = len(grid[0])

    if i + 1 < height:
        neighbours.append((i + 1, j))
    if i - 1 >= 0:
        neighbours.append((i - 1, j))
    if j - 1 >= 0:
        neighbours.append((i, j - 1))
    if j + 1 < width:
        neighbours.append((i, j + 1))

    return neighbours

height = len(puzzle_input)
width = len(puzzle_input[0])

start = (0, 0)
end = (height - 1, width - 1)

min_risk = defaultdict(lambda: float("inf"), {start: 0})

visited = set()

# tuple (cost of path to here, coordinates)
queue = [(0, start)]

while queue:

    node = heappop(queue)

    cumulative_risk, coords = node

    if coords == end:
        print(cumulative_risk)
        break

    visited.add(coords)

    neighbours = adj_squares(puzzle_input, coords[0], coords[1])

    for neighbour in neighbours:
        if neighbour in visited:
            continue

        neighbour_x, neighbour_y = neighbour
        new_risk = cumulative_risk + int(puzzle_input[neighbour_x][neighbour_y])

        if new_risk < min_risk[neighbour]:
            min_risk[neighbour] = new_risk
            heappush(queue, (new_risk, neighbour))