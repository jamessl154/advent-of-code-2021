# https://aochelper2021.blob.core.windows.net/day23/index.html
# http://theory.stanford.edu/~amitp/GameProgramming/MovingObstacles.html
# What to do if we have no more possible moves? (everywhere is blocked)

# Find moves: returns all new valid states of the game and their costs
# Moves to destination are always valid

# When we encounter a "node" or state of the game we need to find all valid moves from this position
# and calculate the cost of moving from the prev state to this state
# and save the state
# If it has no valid moves we remove it

# Valid moves:
# Non-blocked path
# moves ending at spots outside rooms are never valid 
# If this amphipod has moved once it cannot move again until inside its destination
# either at the bottom or on top of an amphipod of the same type

# DFS Move, while spot == '.', if not outside hallway,
# always append move if destination, append other valid moves if not moved already
# can calculate cost just by start - end point coords

class Amber:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 1
class Bronze:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 10
class Copper:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 100
class Desert:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 1000

# forbidden moves are global
forbidden_moves = [(1, 3), (1, 5), (1, 7)]

def dfs_move(row, col, a_map, start, seen=[]):

  if (row, col) in seen:
    return []

  seen.append((row, col))

  if start == False and a_map[row][col] != '.':
    return []

  moves = []

  if start == False and a_map[row][col] == '.':
    if (row, col) not in forbidden_moves:
      moves.append((row, col))

  # down up right left
  for move in dfs_move(row + 1, col, a_map, False, seen):
    moves.append(move)
  for move in dfs_move(row - 1, col, a_map, False, seen):
    moves.append(move)
  for move in dfs_move(row, col + 1, a_map, False, seen):
    moves.append(move)
  for move in dfs_move(row, col - 1, a_map, False, seen):
    moves.append(move)

  return moves

puzzle_input  = [line.replace("\n", "") for line in open('test.txt').readlines()]
print(dfs_move(2, 3, puzzle_input, True))

# def get_all_valid_moves(amphipods, a_map):
#   moves = []

#   for amphipod in amphipods:
#     dfs_move(amphipod.row, amphipod.col, True)

# def main():
#   puzzle_input  = [line.replace("\n", "") for line in open('test.txt').readlines()]
#   # print(puzzle_input)

#   amphipods = []

#   for row in range(len(puzzle_input)):
#     for col in range(len(puzzle_input[row])):
#       match puzzle_input[row][col]:
#         case 'A':
#           amphipods.append(Amber(row, col))
#         case 'B':
#           amphipods.append(Bronze(row, col))
#         case 'C':
#           amphipods.append(Copper(row, col))
#         case 'D':
#           amphipods.append(Desert(row, col))

#   # print(amphipods)
#   # for amphipod in amphipods:
#   #   print(amphipod.row, amphipod.col, type(amphipod).__name__)

# if __name__ == '__main__':
#   main()