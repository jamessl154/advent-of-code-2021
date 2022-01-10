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
    # Amphipods are immobile once moved unless can reach destination
    self.moved = False
    self.energy = 1
    # The destinations for this type of amphipod
    self.secondary_spot = (2,3)
    self.primary_spot = (3,3)
class Bronze:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 10
    self.secondary_spot = (2,5)
    self.primary_spot = (3,5)
class Copper:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 100
    self.secondary_spot = (2,7)
    self.primary_spot = (3,7)
class Desert:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.moved = False
    self.energy = 1000
    self.secondary_spot = (2,9)
    self.primary_spot = (3,9)

# global rule: cannot stop outside of any room 
forbidden_moves = [(1, 3), (1, 5), (1, 7), (1, 9)]

def dfs_move(amphipod, row, col, a_map, seen, start=False):
  # Prevent infinite DFS by returning when visiting a spot already evaluated
  if (row, col) in seen:
    return []
  # add spot to seen list
  seen.append((row, col))
  # We don't want to evaluate the start position, return when we reach a non-empty space
  if start == False and a_map[row][col] != '.':
    return []

  moves = []

  # if this spot is an empty space we can move to
  if a_map[row][col] == '.':
    # must not stop outside of any room
    if (row, col) not in forbidden_moves:
      # destructure primary_spot tuple into row col indices
      a,b = amphipod.primary_spot
      # always allow move to primary_spot
      if (row, col) == amphipod.primary_spot:
        moves.append((row, col))
      # always allow move to secondary_spot if primary spot is correctly filled
      elif (row, col) == amphipod.secondary_spot and type(amphipod) == type(a_map[a][b]):
        moves.append((row, col))
      # Only allow other moves if this amphipod is free to move
      elif amphipod.moved == False:
        moves.append((row, col))

  # down up right left
  for move in dfs_move(amphipod, row + 1, col, a_map, seen):
    moves.append(move)
  for move in dfs_move(amphipod, row - 1, col, a_map, seen):
    moves.append(move)
  for move in dfs_move(amphipod, row, col + 1, a_map, seen):
    moves.append(move)
  for move in dfs_move(amphipod, row, col - 1, a_map, seen):
    moves.append(move)

  return moves

def get_energy_cost(start, end, energy_cost_per_move):
  x_dist = abs(end[0] - start[0])
  y_dist = abs(end[1] - start[1])
  return energy_cost_per_move * (x_dist + y_dist)

assert(get_energy_cost((1,10), (3,3), 100)) == 900

def get_all_valid_moves(amphipods, a_map):
  moves = []
  for amphipod in amphipods:
    # This amphipod's start pos
    start = (amphipod.row, amphipod.col)
    # Find valid moves for this amphipod
    # For each move that exists: include start, end positions and energy cost
    for move in dfs_move(amphipod, amphipod.row, amphipod.col, True):
      # (start, dest, cost)
      moves.append(start, move, get_energy_cost(start, move, amphipod.energy))
  return moves

def main():
  puzzle_input  = [line.replace("\n", "") for line in open('test.txt').readlines()]
  # print(puzzle_input)

  amphipods = []

  for row in range(len(puzzle_input)):
    for col in range(len(puzzle_input[row])):
      match puzzle_input[row][col]:
        case 'A':
          amphipods.append(Amber(row, col))
        case 'B':
          amphipods.append(Bronze(row, col))
        case 'C':
          amphipods.append(Copper(row, col))
        case 'D':
          amphipods.append(Desert(row, col))

  # print(amphipods)
  # for amphipod in amphipods:
  #   print(amphipod.row, amphipod.col, type(amphipod).__name__)

if __name__ == '__main__':
  main()