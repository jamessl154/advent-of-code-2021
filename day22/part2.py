from re import split

with open("test.txt", "r") as f:
  puzzle_input = f.read().splitlines()

on_off_step = [i.split(" ")[0] for i in puzzle_input]

cuboid_step = [split(r',\D=', i.split(" ")[1][2:]) for i in puzzle_input]

cuboid_step = [list(map(lambda x: x.split(".."), i)) for i in cuboid_step]

cuboid_step = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y)), x)), cuboid_step))

# If "on": For each overlapping cuboid, discard overlap, add end result to cuboid list

# If "off": For each cuboid it overlaps with, remove from cuboid list,
# cut the overlapping cuboid into sliced cuboids,
# add all slices to the cuboid list

# safe to sum areas knowing we have no collisions
# For each cuboid in cuboid list, sum += cuboid area, return sum

def sum_area_cuboids(cuboid_list):

  sum = 0

  # cuboid [[x, x], [y, y], [z, z]]
  for cuboid in cuboid_list:
    sum += (cuboid[0][1] - cuboid[0][0] + 1) * (cuboid[1][1] - cuboid[1][0] + 1) * (cuboid[2][1] - cuboid[2][0] + 1)

  return sum

assert sum_area_cuboids([[[10, 12], [10, 12], [10, 12]]]) == 27

# return cuboids in cuboid_map that overlap with the input_cuboid
def overlapping_cuboids(input_cuboid, cuboid_map):

  overlapping_cuboids = []

  # input_cuboid [[10, 12], [10, 12], [10, 12]]
  # cuboid_map [[[11, 13], [11, 13], [11, 13]]]

  for cuboid in cuboid_map:
    # Only way to not overlap is if both points lie outside the range
    if input_cuboid[0][0] < cuboid[0][0] and input_cuboid[0][1] < cuboid[0][0]:
      continue
    if input_cuboid[0][0] > cuboid[0][1] and input_cuboid[0][1] > cuboid[0][1]:
      continue
    if input_cuboid[1][0] < cuboid[1][0] and input_cuboid[1][1] < cuboid[1][0]:
      continue
    if input_cuboid[1][0] > cuboid[1][1] and input_cuboid[1][1] > cuboid[1][1]:
      continue
    if input_cuboid[2][0] < cuboid[2][0] and input_cuboid[2][1] < cuboid[2][0]:
      continue
    if input_cuboid[2][0] > cuboid[2][1] and input_cuboid[2][1] > cuboid[2][1]:
      continue

    # must overlap, add to list
    overlapping_cuboids.append(cuboid)

  return overlapping_cuboids

assert overlapping_cuboids(
  [[10, 10], [10, 10], [10, 10]],
  [[[10, 12], [10, 12], [10, 12]], [[11, 13], [11, 13], [11, 13]], [[9, 11], [9, 11], [9, 11]]]
  ) == [[[10, 12], [10, 12], [10, 12]], [[9, 11], [9, 11], [9, 11]]]

# for each overlapping cuboid, slice() with list of sliced cuboids

# The first slice() gets passed a list with 1 cuboid, that cuboid gets divided,
# slice returns a list of slices and that list is passed on to the next slice()
# until the overlapping cuboids are exhausted

def find_overlap_zone(cuboid_A, cuboid_B):
  # takes 2 cuboids and returns their overlap zone as a cuboid

  a = max(cuboid_A[0][0], cuboid_B[0][0])
  b = min(cuboid_A[0][1], cuboid_B[0][1])

  c = max(cuboid_A[1][0], cuboid_B[1][0])
  d = min(cuboid_A[1][1], cuboid_B[1][1])

  e = max(cuboid_A[2][0], cuboid_B[2][0])
  f = min(cuboid_A[2][1], cuboid_B[2][1])

  return [[a, b], [c, d], [e, f]]

assert find_overlap_zone([[11, 13], [11, 13], [11, 13]], [[10, 12], [10, 12], [10, 12]]) == [[11, 12], [11, 12], [11, 12]]

def fragment_cuboid(overlap_zone, cuboid):
  # deconstructs the cuboid and overlap_zone
  # then rebuilds the cuboid as multiple cuboids and returns them

  # Split cuboid in the x axis, discard non-overlapping pieces into fragments list
  # Result piece split in y axis, " "
  # Result piece split in z axis, " "

  fragments = []
  inner_cuboid = []

  x_boundaries = [cuboid[0][0], cuboid[0][1]]

  for i in overlap_zone[0]:
    if i not in x_boundaries:
      x_boundaries.append(i)

  x_boundaries.sort()

  for x_boundary in range(1, len(x_boundaries)):
    fragment = [[x_boundaries[x_boundary - 1], x_boundaries[x_boundary]], [cuboid[1][0], cuboid[1][1]], [cuboid[2][0], cuboid[2][1]]]

    if x_boundaries[x_boundary - 1] == overlap_zone[0][0]:
      inner_cuboid = fragment
    else:
      fragments.append(fragment)

  cuboid = inner_cuboid

  y_boundaries = [cuboid[1][0], cuboid[1][1]]

  for i in overlap_zone[1]:
    if i not in y_boundaries:
      y_boundaries.append(i)

  y_boundaries.sort()

  for y_boundary in range(1, len(y_boundaries)):
    fragment = [[cuboid[0][0], cuboid[0][1]], [y_boundaries[y_boundary - 1], y_boundaries[y_boundary]], [cuboid[2][0], cuboid[2][1]]]

    if y_boundaries[y_boundary - 1] == overlap_zone[1][0]:
      inner_cuboid = fragment
    else:
      fragments.append(fragment)

  cuboid = inner_cuboid

  z_boundaries = [cuboid[2][0], cuboid[2][1]]

  for i in overlap_zone[2]:
    if i not in z_boundaries:
      z_boundaries.append(i)

  z_boundaries.sort()

  for z_boundary in range(1, len(z_boundaries)):
    fragment = [[cuboid[0][0], cuboid[0][1]], [cuboid[1][0], cuboid[1][1]], [z_boundaries[z_boundary - 1], z_boundaries[z_boundary]]]

    if z_boundaries[z_boundary - 1] == overlap_zone[2][0]:
      inner_cuboid = fragment
    else:
      fragments.append(fragment)

  return fragments

# 2 tests for the fragmenting process
# print(fragment_cuboid([[4, 6], [4, 6], [4, 6]], [[0, 10], [0, 10], [0, 10]]))
# print(fragment_cuboid([[11, 12], [11, 12], [11, 12]], [[11, 13], [11, 13], [11, 13]]))

assert len(fragment_cuboid([[4, 6], [4, 6], [4, 6]], [[0, 10], [0, 10], [0, 10]])) == 6

def add_cuboid_to_cuboid_map(cuboid, cuboid_map, on_off):
  # takes 1 cuboid, slices and returns the cuboids needed for the cuboid map

  overlap_set = overlapping_cuboids(cuboid, cuboid_map)

  cuboids = []

  if on_off == 'on' and not overlap_set:
    return [cuboid]
  if on_off == 'off' and not overlap_set:
    return []

  # if "on" and fully surrounded by overlapping cuboid, return []

  for overlapping_cuboid in overlap_set:

    overlap_zone = find_overlap_zone(overlapping_cuboid, cuboid)

    overlap_fragments = fragment_cuboid(overlap_zone, overlapping_cuboid)

    cuboid_fragments = fragment_cuboid(overlap_zone, cuboid)

    # the overlap fragments are always added
    cuboids.extend(overlap_fragments)

    # the cuboid fragments are only added if "on"
    if on_off == "on":
      cuboids.extend(cuboid_fragments)
      cuboids.append(overlap_zone)

    cuboids.extend(add_cuboid_to_cuboid_map(overlapping_cuboid, cuboids, on_off))

  return cuboids

def main():

  cuboid_map = []

  for i in range(len(cuboid_step)):
    cuboid_map.extend(add_cuboid_to_cuboid_map(cuboid_step[i], cuboid_map, on_off_step[i]))

  print("part2", sum_area_cuboids(cuboid_map))

main()