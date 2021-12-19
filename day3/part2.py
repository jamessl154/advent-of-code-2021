from collections import defaultdict

with open("input.txt", "r") as f:
    puzzle_input = [i.strip() for i in f]

oxygen = puzzle_input.copy()
co2 = puzzle_input.copy()

i = 0

while True:
    temp = []
    oxygen_tracker = defaultdict(int)

    for a in range(len(oxygen)):
        for b in range(len(oxygen[a])):
            if oxygen[a][b] == "1":
                oxygen_tracker[b] += 1

    # case with 2 elements in list oxygen where
    # one index is "0" and the other is "1"
    if oxygen_tracker[i] == len(oxygen) / 2:
        most_common = "1"
    # if majority "1"s at this index
    elif oxygen_tracker[i] > len(oxygen) // 2:
        most_common = "1"
    # else majority "0"s
    else:
        most_common = "0"

    for a in oxygen:
        if a[i] == most_common:
            # only keep the numbers that have the most_common
            # number at this index
            temp.append(a)          

    oxygen = temp.copy()

    i += 1
    if len(oxygen) == 1:
        break

i = 0

while True:
    temp = []

    co2_tracker = defaultdict(int)

    for a in range(len(co2)):
        for b in range(len(co2[a])):
            if co2[a][b] == "1":
                co2_tracker[b] += 1

    if co2_tracker[i] == len(co2) / 2:
        least_common = "0"
    elif co2_tracker[i] > len(co2) // 2:
        least_common = "0"
    else:
        least_common = "1"

    for a in co2:
        if a[i] == least_common:
            temp.append(a)          

    co2 = temp.copy()

    i += 1

    if len(co2) == 1:
        break

print("part2", int(co2[0], 2) * int(oxygen[0], 2))