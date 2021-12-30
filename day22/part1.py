from re import split

with open("input.txt", "r") as f:
  puzzle_input = f.read().splitlines()

on_off = [i.split(" ")[0] for i in puzzle_input]

bounds = [split(r',\D=', i.split(" ")[1][2:]) for i in puzzle_input]

bounds = [list(map(lambda x: x.split(".."), i)) for i in bounds]

bounds = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y)), x)), bounds))

cubes_on = set()

for i in range(len(on_off)):

  if bounds[i][0][0] < -50:
    bounds[i][0][0] = -50
  if bounds[i][0][1] > 50:
    bounds[i][0][1] = 50
  if bounds[i][1][0] < -50:
    bounds[i][1][0] = -50
  if bounds[i][1][1] > 50:
    bounds[i][1][1] = 50
  if bounds[i][2][0] < -50:
    bounds[i][2][0] = -50
  if bounds[i][2][1] > 50:
    bounds[i][2][1] = 50

  if on_off[i] == "on":
    for j in range(bounds[i][0][0], bounds[i][0][1] + 1):
      for k in range(bounds[i][1][0], bounds[i][1][1] + 1):
        for l in range(bounds[i][2][0], bounds[i][2][1] + 1):
            cubes_on.add((j, k, l))

  if on_off[i] == "off":
    for j in range(bounds[i][0][0], bounds[i][0][1] + 1):
      for k in range(bounds[i][1][0], bounds[i][1][1] + 1):
        for l in range(bounds[i][2][0], bounds[i][2][1] + 1):
            cubes_on.discard((j, k, l))

print("part1", len(cubes_on))