puzzle_input = [x for x in open("input.txt").read().splitlines()]

new_input = list(map(lambda x: [char for char in x], puzzle_input))

horizontal_counter = 1

for a in range(4):
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):

            val = int(puzzle_input[i][j]) + horizontal_counter

            if val > 9:
                val -= 9
            new_input[i].append(str(val))

    horizontal_counter += 1

# print(new_input)

temp = new_input.copy()

vertical_counter = 1

for z in range(1, 5):

    for p in range(len(temp)):
        new_input.append([])

    k = z * len(temp) - 1

    for i in range(len(temp)):
        k += 1

        for j in range(len(temp[i])):

            val = int(new_input[i][j]) + vertical_counter
            if val > 9:
                val -= 9
            
            new_input[k].append(str(val))

    vertical_counter += 1

f = open("part2.txt", "w")
for i in range(len(new_input)):
    f.writelines(new_input[i])
    f.write("\n")
f.close()