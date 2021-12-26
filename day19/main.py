import re
from copy import deepcopy

with open("input.txt", "r") as f:
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

# My rotations were wrong: https://github.com/Dullstar/Advent_Of_Code/blob/main/python/year2021/day19_rotations.txt

def orientations_24(scanner):
    """transforms a scanner into a list of 24 scanners for each orientation"""

    # Bot

    # x, y, z orientation
    scanner_list = [scanner]

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0], temp[i][2] = -1 * temp[i][2], temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0] *= -1
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][2] = temp[i][2], -1 * temp[i][0]

    scanner_list.append(temp)

    # Top

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0] *= -1
        temp[i][1] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][2] = -1 * temp[i][2], -1 * temp[i][0]
        temp[i][1] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1] *= -1
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][2] = temp[i][2], temp[i][0]
        temp[i][1] *= -1

    scanner_list.append(temp)

    # Right

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0], temp[i][1], temp[i][2] = temp[i][1], temp[i][2], temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = temp[i][1], -1 * temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = temp[i][1], -1 * temp[i][2], -1 * temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = temp[i][1], temp[i][0]
        temp[i][2] *= -1

    scanner_list.append(temp)

    # Left

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][0], temp[i][1] = -1 * temp[i][1], temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = -1 * temp[i][1], -1 * temp[i][2], temp[i][0]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1] = -1 * temp[i][1], -1 * temp[i][0]
        temp[i][2] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = -1 * temp[i][1], temp[i][2], -1 * temp[i][0]

    scanner_list.append(temp)

    # Back

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][1], temp[i][2] = temp[i][2], -1 * temp[i][1]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = temp[i][2], -1 * temp[i][0], -1 * temp[i][1]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = -1 * temp[i][2], -1 * temp[i][1]
        temp[i][0] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = -1 * temp[i][2], temp[i][0], -1 * temp[i][1]

    scanner_list.append(temp)

    # Front

    temp = deepcopy(scanner)

    for i in range(len(temp)):
        temp[i][1], temp[i][2] = -1 * temp[i][2], temp[i][1]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = -1 * temp[i][2], -1 * temp[i][0], temp[i][1]

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][1], temp[i][2] = temp[i][2], temp[i][1]
        temp[i][0] *= -1

    scanner_list.append(temp)

    temp = deepcopy(scanner)

    for i in range(len(scanner)):
        temp[i][0], temp[i][1], temp[i][2] = temp[i][2], temp[i][0], temp[i][1]

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
            result = ((x_offset, y_offset, z_offset), result)
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

scanner_coordinates = [(0, 0, 0)]

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

                scanner_coordinate, result = result

                scanner_coordinates.append(scanner_coordinate)

                # Add to the scanner map
                scanner_map.append(result)
                
                # remove from missing scanners
                scanners_missing.remove(i)

                for j in result:
                    x, y, z = j
                    # add each beacon of scanner to set
                    full_beacon_set.add((x, y, z))

    full_beacon_set = sorted(full_beacon_set, key=lambda x: x[0])

    print("scanner_coordinates\n", scanner_coordinates)
    print("len(scanner_map)", len(scanner_map))
    print("full_beacon_set\n", full_beacon_set)
    print("part1", len(full_beacon_set))

    manhattan_record = 0

    for i in range(len(scanner_coordinates)):
        for j in range(i, len(scanner_coordinates)):
            if i == j:
                continue
            manhattan_x = abs(scanner_coordinates[i][0] - scanner_coordinates[j][0])
            manhattan_y = abs(scanner_coordinates[i][1] - scanner_coordinates[j][1])
            manhattan_z = abs(scanner_coordinates[i][2] - scanner_coordinates[j][2])
            manhattan_record = max(manhattan_x + manhattan_y + manhattan_z, manhattan_record)

    print("part2", manhattan_record)

main()