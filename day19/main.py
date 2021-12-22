import re
from copy import deepcopy

with open("test.txt", "r") as f:
    puzzle_input = f.read().split("\n\n")

# print(puzzle_input)
puzzle_input = list(map(lambda x: x.split("\n"), puzzle_input))
# print(puzzle_input)
puzzle_input = list(map(lambda x: x[1:], puzzle_input))
# print(puzzle_input)
puzzle_input = list(map(lambda x: list(map(lambda y: y.split(","), x)), puzzle_input))
# print(puzzle_input)
puzzle_input = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y)), x)), puzzle_input))
# print(puzzle_input)

scanner_0 = puzzle_input[0]

scanners = puzzle_input[1:]

# https://docs.python.org/3/library/copy.html#copy.deepcopy

def orientations_24(scanner):
    """transforms a scanner into a list of 24 scanners for each orientation"""

    # Bot

    # x, y, z orientation
    scanner_list = [scanner]

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0] *= -1
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0] *= -1

    scanner_list.append(temp)

    # Top

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0] *= -1
        temp[i][1] *= -1
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0] *= -1
        temp[i][1] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1] *= -1
        temp[i][2] *= -1

    scanner_list.append(temp)

    # Right

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0], temp[i][1] = temp[i][1], -1 * temp[i][0]
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = temp[i][1], temp[i][0]
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = temp[i][1], -1 * temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = temp[i][1], temp[i][0]

    scanner_list.append(temp)

    # Left

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0], temp[i][1] = -1 * temp[i][1], -1 * temp[i][0]
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = -1 * temp[i][1], temp[i][0]
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = -1 * temp[i][1], temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = -1 * temp[i][1], -1 * temp[i][0]

    scanner_list.append(temp)

    # Back

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][1], temp[i][2] = -1 * temp[i][2], -1 * temp[i][1]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = -1 * temp[i][2], -1 * temp[i][1]
        temp[i][0] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = temp[i][2], -1 * temp[i][1]
        temp[i][0] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = temp[i][2], -1 * temp[i][1]

    scanner_list.append(temp)

    # Front

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][1], temp[i][2] = -1 * temp[i][2], temp[i][1]
        temp[i][0] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = temp[i][2], temp[i][1]
        temp[i][0] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = temp[i][2], temp[i][1]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = -1 * temp[i][2], temp[i][1]

    scanner_list.append(temp)

    return scanner_list

# Tests for orientations_24 => use open("scanner.txt", "r")
# for i in orientations_24(scanner_0):
#     print(i[0])

def find12commonbeacons(scanner, base_coord):

    for i in scanner:
        # make relative to base_coord
        x_offset = base_coord[0] - i[0]
        y_offset = base_coord[1] - i[1]
        z_offset = base_coord[2] - i[2]

        temp = deepcopy(scanner)

        for j in temp:
            j[0] += x_offset
            j[1] += y_offset
            j[2] += z_offset

        counter = 0

        for j in scanner_0:
            for k in temp:
                if j == k:
                    counter += 1

        # Found at least 12 common beacons for this scanner
        if counter >= 12:
            return temp

def solve_scanner(scanner, base_coord):

    for i in orientations_24(scanner):

        result = find12commonbeacons(i, base_coord)

        if result:
            return result

full_beacon_list = []

for i in scanner_0:
    for j in scanners:
        result = solve_scanner(j, i)

        if result:
            for k in result:
                full_beacon_list.append(k)

# TypeError: unhashable type: 'list' when converting to set

full_beacon_set = set()

for i in full_beacon_list:
    x, y, z = i[0], i[1], i[2]
    temp = (x, y, z)
    full_beacon_set.add(temp)

print("\nfull_beacon_set\n", full_beacon_set)
print("part1", len(full_beacon_set))