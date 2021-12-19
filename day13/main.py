import matplotlib.pyplot as plt

dots = [x for x in open("test_dots.txt").read().split("\n")]
folds = [x for x in open("test_folds.txt").read().split("\n")]

dots = list(map(lambda x: x.split(","), dots))

folds = list(map(lambda x: x[11:].split("="), folds))

for i in folds:
    i[1] = int(i[1])

# Overlapping dots count are merged and count as 1
# set is useful here as duplicates dont get added
# so we can safely do len(dots_set) to count dots in current image of
# the transparent paper
dots_set = set()

for i in dots:
    # add tuple dot coord to set
    dots_set.add( (int(i[0]), int(i[1])) )

# print(len(dots_set)) # part 1 - after first fold how many dots?

for i in folds:

    # fold left on x axis
    if i[0] == "x":

        fold_line = i[1]

        removed_dots = []
        added_dots = []

        for j in dots_set:
            # Need to mirror dots to the right of this fold_line
            # 2 steps: add mirrored dot to set, remove old dot from set
            if j[0] > fold_line:
                temp = j[0] - fold_line
                new_x = fold_line - temp
                dot = (new_x, j[1])
                added_dots.append(dot)
                removed_dots.append(j)

        for k in removed_dots:
            dots_set.remove(k)
        for l in added_dots:
            dots_set.add(l)

    # fold up on y axis
    if i[0] == "y":

        fold_line = i[1]

        removed_dots = []
        added_dots = []

        for j in dots_set:
            # Need to mirror dots below this fold_line
            # 2 steps: add mirrored dot to set, remove old dot from set
            if j[1] > fold_line:
                temp = j[1] - fold_line
                new_y = fold_line - temp
                dot = (j[0], new_y)
                added_dots.append(dot)
                removed_dots.append(j)

        for k in removed_dots:
            dots_set.remove(k)
        for l in added_dots:
            dots_set.add(l)

    # break # part 1 - after first fold how many dots?

# print(len(dots_set)) # part 1 - after first fold how many dots?

# part 2 - minimize the window to see the 8 capital letters
for i in dots_set:
    plt.plot(i[0], -i[1], 'go--')
plt.show()