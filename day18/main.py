import re
from math import floor, ceil
from collections import deque

with open("input.txt", "r") as f:
    puzzle_input = f.read().splitlines()

# print(puzzle_input)

# https://wiki.python.org/moin/PythonSpeed/PerformanceTips

# https://docs.python.org/3/library/collections.html#collections.deque

def add(a, b):
    temp = []
    temp.append('[')
    temp.append(a)
    temp.append(',')
    temp.append(b)
    temp.append(']')
    return "".join(temp)

numbers = '0123456789'

def explode(snailfish_number, i, j):

    a = i + 1 # i left regular number
    b = j - 1 # j right regular number
    left_pair_number = deque()
    right_pair_number = deque()
    # unknown number of digits here because of previous splits/explosions
    # Guaranteed comma separator to break these loops
    while snailfish_number[a] in numbers:
        left_pair_number.append(snailfish_number[a])
        a += 1
    while snailfish_number[b] in numbers:
        right_pair_number.appendleft(snailfish_number[b])
        b -= 1

    left_pair_number = "".join(left_pair_number)
    right_pair_number = "".join(right_pair_number)

    left = snailfish_number[:i]
    right = snailfish_number[j + 1:]
    snailfish_number = left + "0" + right

    # index i is now "0"

    r_index = i + 1
    r_number = deque()

    while r_index < len(snailfish_number):
        if snailfish_number[r_index] in numbers:

            r_number_left_index = r_index

            # unknown number of digits
            while r_index < len(snailfish_number):
                r_number.append(snailfish_number[r_index])
                # the last r_index here will be in front of the last number
                r_index += 1
                if snailfish_number[r_index] not in numbers:
                    r_number_right_index = r_index
                    break

        # r_number exists
        if r_number:
            break

        r_index += 1

    if r_number:
        r_number = "".join(r_number)
        r_updated_number = int(r_number) + int(right_pair_number)

        snailfish_number = snailfish_number[:r_number_left_index] + str(r_updated_number) + snailfish_number[r_number_right_index:]

    l_index = i - 1
    l_number = deque()

    while l_index > 0:
        if snailfish_number[l_index] in numbers:

            l_number_right_index = l_index + 1

            # unknown number of digits
            while l_index > 0:
                l_number.appendleft(snailfish_number[l_index])
                l_index -= 1

                if snailfish_number[l_index] not in numbers:
                    l_number_left_index = l_index + 1
                    break

        # found l_number
        if l_number:
            break

        l_index -= 1

    if l_number:
        l_number = "".join(l_number)
        l_updated_number = int(l_number) + int(left_pair_number)
        snailfish_number = snailfish_number[:l_number_left_index] + str(l_updated_number) + snailfish_number[l_number_right_index:]

    return snailfish_number

# Tests for explode
# print(explode("[[[[[9,8],1],2],3],4]", 4, 8)) # expect [[[[0,9],2],3],4]
# print(explode("[7,[6,[5,[4,[3,2]]]]]", 12, 16)) # expect [7,[6,[5,[7,0]]]]
# print(explode("[[6,[5,[4,[3,2]]]],1]", 10, 14)) # expect [[6,[5,[7,0]]],3]
# print(explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", 10, 14)) # expect [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
# print(explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", 24, 28)) # expect [[3,[2,[8,0]]],[9,[5,[7,0]]]]

def split(snailfish_number, i, j):

    split_num = int(snailfish_number[i:j + 1])

    left_split_pair = floor(split_num / 2)
    right_split_pair = ceil(split_num / 2)

    split_pair = []

    split_pair.append("[")
    split_pair.append(str(left_split_pair))
    split_pair.append(",")
    split_pair.append(str(right_split_pair))
    split_pair.append("]")

    snailfish_number = snailfish_number[:i] + "".join(split_pair) + snailfish_number[j + 1:]

    return snailfish_number

def split_test(snailfish_number):

        counter = 0

        for i in range(len(snailfish_number)):
            if snailfish_number[i] in numbers:

                counter += 1

                if counter > 1:

                    j = i

                    while snailfish_number[j] in numbers:
                        j += 1

                    left_index_num = i - 1
                    right_index_num = j - 1
                    return (True, left_index_num, right_index_num)
            else:
                counter = 0

        return (False, 0, 0)

# Tests for split_test
# print(split_test("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")) # expect (True, 22, 23)
# print(split_test("[[[[0,7],4],[15,[0,13]]],[1,1]]")) # expect (True, 13, 14)

def reduce(snailfish_number):

    while True:
        # explodes?
        open_bracket = 0
        for i in range(len(snailfish_number)):
            if snailfish_number[i] == "[":
                open_bracket += 1
            if snailfish_number[i] == "]":
                open_bracket -= 1
            if open_bracket == 5:
                left_bracket = i
                j = i + 1
                # Exploding pairs will always consist of two regular numbers
                while snailfish_number[j] != "]":
                    j += 1
                right_bracket = j
                break

        if open_bracket == 5:
            snailfish_number = explode(snailfish_number, i, j)
            continue

        # splits?
        result, i, j = split_test(snailfish_number)
        
        if result == True:
            snailfish_number = split(snailfish_number, i, j)
            continue

        break
    
    return snailfish_number

def magnitude(snailfish_number):

    # single regular number
    if len(snailfish_number) == 1 and snailfish_number[0] in numbers:
        return int(snailfish_number[0])
    # pair of regular numbers
    if re.search(r"^\[\d+,\d+\]$", snailfish_number):
        return int(snailfish_number[1]) * 3 + int(snailfish_number[3]) * 2

    open_bracket = 0

    comma_separator = 0

    # find the comma
    for i in range(len(snailfish_number)):
        if snailfish_number[i] == "[":
            open_bracket += 1
        if snailfish_number[i] == "]":
            open_bracket -= 1
        if open_bracket == 1 and snailfish_number[i] == ",":
            result = magnitude(snailfish_number[1:i]) * 3 + magnitude(snailfish_number[i + 1:len(snailfish_number) - 1]) * 2
            return result

# Tests for magnitude
# print(magnitude("[[1,2],[[3,4],5]]")) # expect 143
# print(magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")) # expect 1384
# print(magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]")) # expect 445
# print(magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]")) # expect 791
# print(magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]")) # expect 1137
# print(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")) # expect 3488

# initial reduction
result = add(puzzle_input[0], puzzle_input[1])
result = reduce(result)

for i in range(2, len(puzzle_input)):
    result = add(result, puzzle_input[i])
    result = reduce(result)

print("part1", magnitude(result))

record = 0

# Non commutative addition for snailfish numbers
for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input)):
        if i == j:
            continue
        temp = add(puzzle_input[i], puzzle_input[j])
        temp = reduce(temp)
        record = max(magnitude(temp), record)

print("part2", record)