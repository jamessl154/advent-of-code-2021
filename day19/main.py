import re
from copy import deepcopy

with open("scanner.txt", "r") as f:
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

