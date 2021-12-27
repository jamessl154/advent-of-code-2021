from collections import defaultdict
from copy import deepcopy

with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n\n")

image_enhancement_algorithm = puzzle_input[0].replace("\n", "")

input_image = puzzle_input[1].split("\n")

pixel_dict = defaultdict(lambda: defaultdict(int))

# initialize pixel dict
for i in range(len(input_image)):
    for j in range(len(input_image[i])):
        if input_image[i][j] == "#":
            pixel_dict[i][j] = 1

def to_binary_string_3x3(i, j, min_row, max_row, min_col, max_col, sequences):
    temp = []

    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if sequences % 2 != 0:
                if a < min_row or a > max_row:
                    temp.append("1")
                elif b < min_col or b > max_col:
                    temp.append("1")
                else:
                    temp.append(str(pixel_dict[a][b]))
            else:
                temp.append(str(pixel_dict[a][b]))

    return "".join(temp)

sequences = 0

# part1 sequences < 2
while sequences < 50:

    pixel_changes = []

    pixel_dict_copy = deepcopy(pixel_dict)

    min_row = 0
    max_row = 0
    min_col = 0
    max_col = 0

    for i in pixel_dict:
        for j in pixel_dict[i]:
            if pixel_dict[i][j] == 1:
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    for i in range(min_row - 1, max_row + 2):
        for j in range(min_col - 1, max_col + 2):

            binary_string = to_binary_string_3x3(i, j, min_row, max_row, min_col, max_col, sequences)

            binary_index = int(binary_string, 2)

            output_pixel = image_enhancement_algorithm[binary_index]

            if output_pixel == '#':
                pixel_changes.append((1, (i, j)))

    pixel_dict.clear()

    for i in pixel_changes:
        pixel, coords = i
        x, y = coords

        pixel_dict[x][y] = pixel

    sequences += 1

lit_pixels = 0

for i in pixel_dict:
    for j in pixel_dict[i]:
        if pixel_dict[i][j] == 1:
            lit_pixels += 1

print("part2", lit_pixels)