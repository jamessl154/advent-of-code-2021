puzzle_input = [x for x in open("input.txt").read().split("\n")]

# print(puzzle_input)

low_points = []

for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[i])):

        temp = []

        # Bounds checks
        if int(j) - 1 >= 0:
            temp.append(puzzle_input[i][j - 1])
        if int(j) + 1 < len(puzzle_input[i]):
            temp.append(puzzle_input[i][j + 1])
        if int(i) - 1 >= 0:
            temp.append(puzzle_input[i - 1][j])
        if int(i) + 1 < len(puzzle_input):
            temp.append(puzzle_input[i + 1][j])

        adjacent_squares = len(temp)

        counter = 0

        for k in temp:
            if int(puzzle_input[i][j]) < int(k):
                counter += 1

        if counter == adjacent_squares:
            low_points.append((i, j))

sum_risk_low_points = 0

for i in low_points:
    j, k = i
    sum_risk_low_points += int(puzzle_input[j][k]) + 1

print("part1", sum_risk_low_points)

class Point:

    def __init__(self, value):
        self.value = value
        self.adjacent_points = []
        self.visited = False

    def append_point(self, point):
        self.adjacent_points.append(point)


points_list = []

for i in range(len(puzzle_input)):

    points_list.append([])

    for j in range(len(puzzle_input[i])):
        point = Point(puzzle_input[i][j])
        points_list[i].append(point)

for i in range(len(points_list)):
    for j in range(len(points_list[i])):
        
        p = points_list[i][j]

        # up
        if i - 1 >= 0 and points_list[i-1][j].value != "9":
            p.append_point(points_list[i-1][j])
        # down
        if i + 1 < len(points_list) and points_list[i+1][j].value != "9":
            p.append_point(points_list[i+1][j])
        # left
        if j - 1 >= 0 and points_list[i][j-1].value != "9":
            p.append_point(points_list[i][j-1])
        # right
        if j + 1 < len(points_list[i]) and points_list[i][j+1].value != "9":
            p.append_point(points_list[i][j+1])

# https://en.wikipedia.org/wiki/Flood_fill

queue = []

result = []

for point in low_points:

    x = point[0]
    y = point[1]

    queue.append(points_list[x][y])

    counter = 0

    while queue:

        n = queue.pop(0)
        n.visited = True
        counter += 1
        
        for i in n.adjacent_points:
            if i.visited == False:
                i.visited = True
                queue.append(i)
    
    result.append(counter)

# print(low_points)
result = sorted(result, reverse=True)
# print(result)
print("part2", result[0] * result[1] * result[2])