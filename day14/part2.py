from collections import Counter, defaultdict

puzzle_input = [x for x in open("input.txt").read().splitlines()]

polymer_template = puzzle_input[0]

insertion_rules = puzzle_input[2:]

matches = list(map(lambda x: x[:2], insertion_rules))
inserts = list(map(lambda x: x[-1], insertion_rules))

# print(polymer_template)
# print(matches)
# print(inserts)

a = Counter()

b = Counter()

# step 0 add base pairs to a counter
for i in range(len(polymer_template) - 1):
    pair = polymer_template[i:i+2]
    a[pair] += 1

# step 0 add base letters to b counter
for i in polymer_template:
    b[i] += 1

i = 0

while (i < 40):

    temp = Counter()

    for pair in a:
        # matches and inserts lists share indices e.g. matches[7] NN -> C inserts[7]
        # So we can find the letter using the index of the 2 letter string in matches list that == pair
        insert = inserts[matches.index(pair)]

        # Replicating doing "a[pair]" number of inserts of character "insert"
        # add to the letter counter b
        b[insert] += a[pair]

        # NN => N + C, C + N
        left_pair = pair[0] + insert
        right_pair = insert + pair[1]

        # For each occurrence of "pair" in the previous gen, we add those
        # occurrences to left_pair and right_pair in new gen
        temp[left_pair] += a[pair]
        temp[right_pair] += a[pair]

    # overwrite "a" at each step e.g. NN's children are NC and CN excluding NN
    a = temp
    i += 1

# print(a)
# print(b)

d = b.most_common()[0]
e = b.most_common()[-1]

print(d)
print(e)

print(d[1] - e[1])