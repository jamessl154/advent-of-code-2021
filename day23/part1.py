puzzle_input  = [line.replace("\n", "") for line in open('test.txt').readlines()]

print(puzzle_input)

# class Space:
#   def __init__(self, blocked):
#     self.blocked = blocked

#   def invert_blocked():
#     self.blocked = not blocked

class Amphipod:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def up():
    self.x -= 1
  def down():
    self.x += 1
  def left():
    self.y -= 1
  def right():
    self.y += 1

class Amber(Amphipod):

  # global if 3,3 filled

  def __init__(self, x, y):
    # call super
    Amphipod.__init__(self, x, y)
    self.cost = 1
    # goal
    # 2, 3 if Amber at 3, 3
    # 3, 3

class Bronze(Amphipod):

  # global if 3,5 filled

  def __init__(self, x, y):
    Amphipod.__init__(self, x, y)
    self.cost = 10
    # goal
    # 2, 5 if Bronze at 3, 5
    # 3, 5

class Copper(Amphipod):

  # global if 3,7 filled

  def __init__(self, x, y):
    Amphipod.__init__(self, x, y)
    self.cost = 100
    # goal
    # 2, 7 if Copper at 3, 7
    # 3, 7

class Desert(Amphipod):

  # global if 3,9 filled

  def __init__(self, x, y):
    Amphipod.__init__(self, x, y)
    self.cost = 1000
    # goal
    # 2, 9 if Desert at 3, 9
    # 3, 9

def main():
  amphipod_map = []

  for row in range(len(puzzle_input)):
    amphipod_map.append([])
    for column in range(len(puzzle_input[row])):
      if puzzle_input[row][column] == 'A':
        amphipod_map[row].append(Amber(row, column))
      elif puzzle_input[row][column] == 'B':
        amphipod_map[row].append(Bronze(row, column))
      elif puzzle_input[row][column] == 'C':
        amphipod_map[row].append(Copper(row, column))
      elif puzzle_input[row][column] == 'D':
        amphipod_map[row].append(Desert(row, column))
      elif puzzle_input[row][column] == '#':
        amphipod_map[row].append('#')
      else:
        amphipod_map[row].append(None)

  # print(amphipod_map)
  # for row in amphipod_map:
  #   for amphipod in row:
  #     if amphipod:
  #       print(amphipod,"pos", amphipod.x, amphipod.y,"cost" , amphipod.cost)

main()