puzzle_input = [x for x in open("test.txt").read().split("\n")]

# print(puzzle_input)

temp = list(map(lambda x: x.split(" | "), puzzle_input))

# print(temp)

data = list(map(lambda x: [x[0].split(" "), x[1].split(" ")], temp))

# print(data)

def length(word):
    return len(word)

result = []

part1_sum = 0

# part1
for i in data:
    for j in i[1]:
        if len(j) == 2:
            part1_sum += 1

        if len(j) == 4:
            part1_sum += 1

        if len(j) == 3:
            part1_sum += 1

        if len(j) == 7:
            part1_sum += 1

# part2
for i in data:
    keys = [-1] * 10

    i[0].sort(key=length)

    for j in i[0]:
        if len(j) == 2:
            keys[1] = j

        if len(j) == 4:
            keys[4] = j

        if len(j) == 3:
            keys[7] = j

        if len(j) == 7:
            keys[8] = j

        if len(j) == 6:
            for m in keys[1]:
                if m not in j:
                    keys[6] = j
                    c = m

    for y in i[0]:
        if len(y) == 5:
            if c not in y:
                keys[5] = y

        if len(y) == 6:
            counter = 0
            for k in keys[5]:
                if k in y:
                    counter += 1
            
            if counter == 5:
                if c in y:
                    keys[9] = y

    for j in keys[6]:
        if j not in keys[5]:
            e = j

    for j in i[0]:
        if len(j) == 5 and e in j:
            keys[2] = j

    for j in i[0]:
        if len(j) == 5 and j != keys[5] and j != keys[2]:
            keys[3] = j

    for l in i[0]:
        if l not in keys:
            keys[0] = l
            break

    sum_string = ''

    for j in i[1]:
        compare_a = sorted(j, key=lambda x: (str.lower(x), x))
        formatA = "".join(compare_a)

        for h in range(len(keys)):

            compare_b = sorted(keys[h], key=lambda x: (str.lower(x), x))
            formatB = "".join(compare_b)

            if formatA == formatB:
                sum_string += str(h)

    result.append(sum_string)
    # print(keys, i)


end_sum = 0

for i in result:
    end_sum += int(i)


print("part1", part1_sum)
print("part2", end_sum)