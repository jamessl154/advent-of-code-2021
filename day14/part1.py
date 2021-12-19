from collections import Counter

puzzle_input = [x for x in open("input.txt").read().splitlines()]

polymer_template = puzzle_input[0]

insertion_rules = puzzle_input[2:]

matches = list(map(lambda x: x[:2], insertion_rules))
inserts = list(map(lambda x: x[-1], insertion_rules))

# print(matches, inserts)

# As we iterate through and insert we are displacing indices
# by the number of previous insertions

# need a counter of number insertions
# for each new insertion in polymer_template
# insert at "index of match" + counter

# https://docs.python.org/3/tutorial/datastructures.html

k = 0

while (k < 10):

    to_be_inserted = []

    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i] + polymer_template[i+1]

        for j in range(len(matches)):
            if pair == matches[j]:
                # len(to_be_inserted) is the counter here
                to_be_inserted.append((i + 1 + len(to_be_inserted), j))

    for i in to_be_inserted:
        polymer_template = polymer_template[:i[0]] + inserts[i[1]] + polymer_template[i[0]:]
    
    k += 1

# print(polymer_template)

a = Counter()

# https://docs.python.org/3/library/collections.html#collections.Counter

for i in polymer_template:
    a[i] += 1

b = a.most_common()[0]
c = a.most_common()[-1]

print(b)
print(c)

print(b[1] - c[1])