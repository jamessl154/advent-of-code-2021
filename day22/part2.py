from re import split

with open("test.txt", "r") as f:
  puzzle_input = f.read().splitlines()

on_off_step = [i.split(" ")[0] for i in puzzle_input]

cuboid_step = [split(r',\D=', i.split(" ")[1][2:]) for i in puzzle_input]

cuboid_step = [list(map(lambda x: x.split(".."), i)) for i in cuboid_step]

cuboid_step = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y)), x)), cuboid_step))

# If "on": For each overlapping cuboid, remove from the cuboid_map
# cut into pieces, discard overlap, add all pieces to the cuboid_map

# If "off": For each overlapping cuboid, remove from cuboid map,
# cut into pieces, discard overlap and input cuboid, add remaining
# pieces to the cuboid map

def sum_area_cuboids(cuboid_map):
  # For each cuboid in cuboid map, sum += cuboid area, return sum
  # safe to sum areas once we know we have no collisions

  sum = 0

  # cuboid [[x, x], [y, y], [z, z]]
  for cuboid in cuboid_map:
    sum += (cuboid[0][1] - cuboid[0][0] + 1) * (cuboid[1][1] - cuboid[1][0] + 1) * (cuboid[2][1] - cuboid[2][0] + 1)

  return sum

assert sum_area_cuboids([[[10, 12], [10, 12], [10, 12]]]) == 27

def find_overlapping_cuboids(input_cuboid, cuboids):
  # returns a list of the cuboids that overlap the input_cuboid

  overlapping_cuboids = []

  # input_cuboid [[10, 12], [10, 12], [10, 12]]
  # cuboids [[[11, 13], [11, 13], [11, 13]]]

  for cuboid in cuboids:
    # Only way to not overlap is if both points lie outside the range
    # checking 1 bound only as cuboid[0][0] <= cuboid[0][1]
    if input_cuboid[0][1] < cuboid[0][0]:
      continue
    if input_cuboid[0][0] > cuboid[0][1]:
      continue
    if input_cuboid[1][1] < cuboid[1][0]:
      continue
    if input_cuboid[1][0] > cuboid[1][1]:
      continue
    if input_cuboid[2][1] < cuboid[2][0]:
      continue
    if input_cuboid[2][0] > cuboid[2][1]:
      continue

    # cuboid must overlap, add to list
    overlapping_cuboids.append(cuboid)

  return overlapping_cuboids

assert find_overlapping_cuboids(
  [[10, 10], [10, 10], [10, 10]],
  [[[10, 12], [10, 12], [10, 12]], [[11, 13], [11, 13], [11, 13]], [[9, 11], [9, 11], [9, 11]]]
  ) == [[[10, 12], [10, 12], [10, 12]], [[9, 11], [9, 11], [9, 11]]]

def find_overlap_zone(cuboid_A, cuboid_B):
  # takes 2 cuboids and returns their overlap zone as a cuboid.
  # For each overlapping cuboid we are assuming single overlap zone,
  # asserting it's impossible for the same 2 cuboids to overlap more than once

  a = max(cuboid_A[0][0], cuboid_B[0][0])
  b = min(cuboid_A[0][1], cuboid_B[0][1])

  c = max(cuboid_A[1][0], cuboid_B[1][0])
  d = min(cuboid_A[1][1], cuboid_B[1][1])

  e = max(cuboid_A[2][0], cuboid_B[2][0])
  f = min(cuboid_A[2][1], cuboid_B[2][1])

  return [[a, b], [c, d], [e, f]]

assert find_overlap_zone([[11, 13], [11, 13], [11, 13]], [[10, 12], [10, 12], [10, 12]]) == [[11, 12], [11, 12], [11, 12]]

def fragment_cuboid(overlap_zone, cuboid):
  # deconstructs the cuboid and the overlap_zone
  # then rebuilds the cuboid as multiple cuboids and returns them

  # Split cuboid in the x axis, discard non-overlapping pieces into fragments list
  # Result piece split in y axis, " "
  # Result piece split in z axis, " "
  # return fragments

  fragments = []
  inner_cuboid = []

  x_boundaries = [cuboid[0][0], cuboid[0][1]]

  for boundary in overlap_zone[0]:
    if boundary not in x_boundaries:
      x_boundaries.append(boundary)

  # test.txt, error where the overlap zone is 1 square wide [[5, 5], ... ]
  if overlap_zone[0][0] == overlap_zone[0][1]:
    x_boundaries.append(overlap_zone[0][0])

  x_boundaries.sort()

  for x_boundary in range(1, len(x_boundaries)):
    fragment = [[x_boundaries[x_boundary - 1], x_boundaries[x_boundary]], [cuboid[1][0], cuboid[1][1]], [cuboid[2][0], cuboid[2][1]]]

    # if this piece contains the overlap zone, we separate
    if x_boundaries[x_boundary - 1] == overlap_zone[0][0]:
      inner_cuboid = fragment
    else:
      # otherwise it is a fragment, add to fragments list
      fragments.append(fragment)

  cuboid = inner_cuboid

  y_boundaries = [cuboid[1][0], cuboid[1][1]]

  for boundary in overlap_zone[1]:
    if boundary not in y_boundaries:
      y_boundaries.append(boundary)

  y_boundaries.sort()

  for y_boundary in range(1, len(y_boundaries)):
    fragment = [[cuboid[0][0], cuboid[0][1]], [y_boundaries[y_boundary - 1], y_boundaries[y_boundary]], [cuboid[2][0], cuboid[2][1]]]

    if y_boundaries[y_boundary - 1] == overlap_zone[1][0]:
      inner_cuboid = fragment
    else:
      fragments.append(fragment)

  cuboid = inner_cuboid

  z_boundaries = [cuboid[2][0], cuboid[2][1]]

  for boundary in overlap_zone[2]:
    if boundary not in z_boundaries:
      z_boundaries.append(boundary)

  z_boundaries.sort()

  for z_boundary in range(1, len(z_boundaries)):
    fragment = [[cuboid[0][0], cuboid[0][1]], [cuboid[1][0], cuboid[1][1]], [z_boundaries[z_boundary - 1], z_boundaries[z_boundary]]]

    if z_boundaries[z_boundary - 1] == overlap_zone[2][0]:
      pass
    else:
      fragments.append(fragment)

  # don't return the overlap zone because its already found from find_overlap_zone()
  return fragments

# Tests for fragment_cuboid
# print(fragment_cuboid([[4, 6], [4, 6], [4, 6]], [[0, 10], [0, 10], [0, 10]]))
# print(fragment_cuboid([[11, 12], [11, 12], [11, 12]], [[11, 13], [11, 13], [11, 13]]))

assert len(fragment_cuboid([[4, 6], [4, 6], [4, 6]], [[0, 10], [0, 10], [0, 10]])) == 6

def is_fully_overlapped(cuboid, cuboid_map):
  # return boolean depending on if this cuboid is fully overlapped by any cuboid in the cuboid map

  for map_cuboid in cuboid_map:

    x_range = range(map_cuboid[0][0], map_cuboid[0][1] + 1)
    y_range = range(map_cuboid[1][0], map_cuboid[1][1] + 1)
    z_range = range(map_cuboid[2][0], map_cuboid[2][1] + 1)

    if cuboid[0][0] in x_range and cuboid[0][1] in x_range:
      if cuboid[1][0] in y_range and cuboid[1][1] in y_range:
        if cuboid[2][0] in z_range and cuboid[2][1] in z_range:
          return True

def resolve_overlapping_cuboids(cuboid, cuboid_map, on_off, overlap_set):
  # First need to gather cuboids into a list to be removed, finally remove after all overlapping cuboids resolved

  if on_off == 'on':
    on_off = 'off'
  elif on_off == 'off':
    on_off = 'on'

  overlapping_cuboids_map = []

  overlapping_cuboids_map.extend(add_cuboid_to_cuboid_map(overlap_set[0], [cuboid], on_off))
  cuboid_map.remove(overlap_set[0])
  overlap_set.remove(overlap_set[0])

  for overlapping_cuboid in overlap_set:
    # remove from the cuboid map, process into fragments, add fragments back
    cuboid_map.remove(overlapping_cuboid)
    overlapping_cuboids_map.extend(add_cuboid_to_cuboid_map(overlapping_cuboid, overlapping_cuboids_map, on_off))

  return overlapping_cuboids_map

def add_cuboid_to_cuboid_map(cuboid, cuboid_map, on_off):
  # takes 1 cuboid input step, evaluates it by
  # slicing it and overlapping cuboids if necessary,
  # returns resultant cuboids

  overlap_set = find_overlapping_cuboids(cuboid, cuboid_map)

  cuboids = []

  # if "on" and fully surrounded by overlapping cuboid, result cuboids are empty, avoids unecessary evaluation
  if on_off == 'on' and is_fully_overlapped(cuboid, cuboid_map) == True:
    return []
  # no overlapping cuboids and "on"
  if on_off == 'on' and not overlap_set:
    return [cuboid]
  # no overlapping cuboids and "off"
  if on_off == 'off' and not overlap_set:
    return []

  # 1 overlapping cuboid
  if len(overlap_set) == 1:
    # Remove the overlapping cuboid from the cuboid_map
    cuboid_map.remove(overlap_set[0])

    overlap_zone = find_overlap_zone(overlap_set[0], cuboid)

    overlap_fragments = fragment_cuboid(overlap_zone, overlap_set[0])

    cuboid_fragments = fragment_cuboid(overlap_zone, cuboid)

    # the overlapping cuboid's fragments are always added back
    cuboids.extend(overlap_fragments)

    # the input cuboid fragments and overlap zone are only added if "on"
    if on_off == "on":
      cuboids.extend(cuboid_fragments)
      cuboids.append(overlap_zone)

    return cuboids

  # more than 1 overlapping cuboid
  result_cuboids = resolve_overlapping_cuboids(cuboid, cuboid_map, on_off, overlap_set)

  cuboids.extend(result_cuboids)

  return cuboids

def main():
  # adds each cuboid_step to a cuboid_map, resolving collisions and finally summing the area

  cuboid_map = []

  for step_index in range(len(cuboid_step)):
    cuboids = add_cuboid_to_cuboid_map(cuboid_step[step_index], cuboid_map, on_off_step[step_index])
    cuboid_map.extend(cuboids)

  print("part2", sum_area_cuboids(cuboid_map))

main()