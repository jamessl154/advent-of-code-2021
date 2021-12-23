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

scanners = puzzle_input

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
# for i in orientations_24(scanners[0]):
#     print(i[0])

def check_match_in_scanner_map(scanner):

    for i in range(len(scanner_map)):

        # reset counter after each scanner
        counter = 0

        for j in scanner:
            if j in scanner_map[i]:
                counter += 1

        if counter >= 12:
            return scanner

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

        result = check_match_in_scanner_map(temp)
        if result:
            return result

def solve_scanner(scanner, base_coord):

    for orientation in orientations_24(scanner):

        result = find12commonbeacons(orientation, base_coord)

        if result:
            return result

def add_scanner_to_map(scanner, full_beacon_set):

    # for all beacons in a scanners 24 orientations,
    # if that beacon points to a beacon in the set, does
    # that scanner share 12 common beacons?

    for base_coord in full_beacon_set:

        result = solve_scanner(scanner, base_coord)

        if result:
            return result

scanner_map = [scanners[0]]

# keeps track of which scanners are not in the map by their index in scanners
scanners_missing = []

for i in range(1, len(scanners)):
    scanners_missing.append(i)

def main():

    # keeps tracks of all unique points in 3d region relative to scanners[0] at 0,0,0
    full_beacon_set = set()

    # initially the region only contains scanners[0]'s beacons
    for i in scanners[0]:
        x, y, z = i
        full_beacon_set.add((x, y, z))

    while scanners_missing:

        # Try to add each scanner to the scanner_map 1 at a time
        for i in scanners_missing:

            result = add_scanner_to_map(scanners[i], full_beacon_set)

            if result:

                # Add to the scanner map
                scanner_map.append(result)

                # remove from missing scanners
                scanners_missing.remove(i)

                for j in result:
                    x, y, z = j
                    # add each beacon of scanner to set
                    full_beacon_set.add((x, y, z))

    full_beacon_set = sorted(full_beacon_set, key=lambda x: x[0])

    print(len(scanner_map))
    print("full_beacon_set\n", full_beacon_set)
    print("part1", len(full_beacon_set))

main()