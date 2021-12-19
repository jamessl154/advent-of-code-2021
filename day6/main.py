with open('input.txt') as f:
    puzzle_input = f.read().split(",")

# print(puzzle_input)

temp = list(map(lambda x: int(x), puzzle_input))

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0

for i in temp:
    if i == 1:
        one += 1
    if i == 2:
        two += 1
    if i == 3:
        three += 1
    if i == 4:
        four += 1
    if i == 5:
        five += 1

# print(one, two, three, four, five)

i = 0

# part 1: i < 80
while i < 256:

    zero_temp = zero

    zero = one
    one = two
    two = three
    three = four
    four = five
    five = six
    six = zero_temp + seven
    seven = eight
    eight = zero_temp

    i += 1

print(zero + one + two + three + four + five + six + seven + eight)