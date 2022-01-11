from collections import defaultdict
from heapq import heappush, heappop

# Great Visualiser: https://aochelper2021.blob.core.windows.net/day23/index.html

# global rule: cannot stop outside of any room
forbidden_moves = [16, 18, 20, 22]

# global amphipod goals, values are the indices of the correct side room positions for key amphipod
amphipod_goals = {
  'A': [29, 42],
  'B': [31, 44],
  'C': [33, 46],
  'D': [35, 48]
}

# global hallway 14-24
hallway = range(14, 25)

def dfs_move(spot_index, amphipod, start_index, a_map, seen, start=False):
  # Prevent infinite DFS by returning when visiting a spot already evaluated
  if spot_index in seen:
    return []
  # add spot_index to seen list
  seen.append(spot_index)
  # We don't want to evaluate the start position
  if start == True:
    pass
  # return when we reach a non-empty space
  elif a_map[spot_index] != '.':
    return []

  moves = []

  # empty space found
  if a_map[spot_index] == '.':
    # can't stop directly outside a room
    if spot_index not in forbidden_moves:
      back_of_side_room_index = amphipod_goals[amphipod][1]
      # always allow move to the back of the side room
      if spot_index == back_of_side_room_index:
        moves.append(spot_index)
      # allow move to index 0 of amphipod_goals, the front of the side room, if the back is filled with the same amphipod
      elif spot_index == amphipod_goals[amphipod][0] and a_map[back_of_side_room_index] == amphipod:
        moves.append(spot_index)
      # all amphipods starting in the hallway have already moved and cannot move unless into their destination
      elif start_index not in hallway:
        moves.append(spot_index)

  # down up right left
  for move in dfs_move(spot_index + 13, amphipod, start_index, a_map, seen):
    moves.append(move)
  for move in dfs_move(spot_index - 13, amphipod, start_index, a_map, seen):
    moves.append(move)
  for move in dfs_move(spot_index + 1, amphipod, start_index, a_map, seen):
    moves.append(move)
  for move in dfs_move(spot_index - 1, amphipod, start_index, a_map, seen):
    moves.append(move)

  return moves

def get_energy_cost(amphipod, old_index, new_index):
  energy_cost_per_move = 0
  match amphipod:
    case 'A':
      energy_cost_per_move = 1
    case 'B':
      energy_cost_per_move = 10
    case 'C':
      energy_cost_per_move = 100
    case 'D':
      energy_cost_per_move = 1000
  diff = abs(new_index - old_index)
  vertical_distance = diff // 13
  horizontal_distance = diff % 13
  return (vertical_distance + horizontal_distance) * energy_cost_per_move

def create_new_state(str_amphipod_map, old_index, new_index):
  list_amphipod_map = list(str_amphipod_map)
  list_amphipod_map[old_index], list_amphipod_map[new_index] = list_amphipod_map[new_index], list_amphipod_map[old_index]
  return "".join(list_amphipod_map)

def get_all_valid_moves(amphipod_map):
  moves = []
  for spot_index in range(len(amphipod_map)):
    # alphabetical test, ABCD amphipods
    if amphipod_map[spot_index].isalpha():
      amphipod = amphipod_map[spot_index]
      # can return empty list if no valid moves
      for move in dfs_move(spot_index, amphipod, spot_index, amphipod_map, [], True):
        new_index = move
        # create new string by swapping the old with new index, we only ever move amphipod to empty space '.' 
        new_state = create_new_state(amphipod_map, spot_index, new_index)
        # get the energy cost of the move and append tuple to moves list
        moves.append((get_energy_cost(amphipod, spot_index, new_index), new_state))
  return moves

def main():
  puzzle_input  = "".join([line.replace("\n", "") for line in open('test.txt').readlines()])

  start = puzzle_input
  end = '##############...........####A#B#C#D###  #A#B#C#D#    #########  '

  # Nodes that are the same will have the same amphipod map
  # Would they also have the same moved amphipods?
  # No, if our moves are always valid the only way to get to that state would be moving
  visited = set()

  queue = [(0, start)]

  # creates a defaultdict with default value (tentative energy value) as infinity
  # except {start: 0}, the energy cost of the initial state is zero
  min_energy_cost = defaultdict(lambda: float("inf"), {start: 0})

  while queue:

    node = heappop(queue)

    cumulative_energy, state = node

    # if state represents the end game state
    if state == end:
      print(cumulative_energy)
      return

    visited.add(state)

    next_states = get_all_valid_moves(state)
    # get_all_valid moves should return a list of tuples that represents all valid next states from this state
    # each tuple consists of:
    #   first argument energy cost of going from old to new state
    #   second argument the new state as a string

    # can reach dead end if no next states, the next node from the queue will then be evaluated
    for next_state in next_states:
      energy_cost, state = next_state
      if state in visited:
        continue
      new_energy_cost = cumulative_energy + energy_cost
      if new_energy_cost < min_energy_cost[state]:
        min_energy_cost[state] = new_energy_cost
        heappush(queue, (new_energy_cost, state))

  # if the queue empties then the problem is unsolvable
  print("unsolvable")

if __name__ == '__main__':
  main()