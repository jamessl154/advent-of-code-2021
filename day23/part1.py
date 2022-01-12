from collections import defaultdict
from heapq import heappush, heappop
# Great Visualiser: https://aochelper2021.blob.core.windows.net/day23/index.html

# global forbidden moves, cannot stop outside of any room
forbidden_moves = [16, 18, 20, 22]
# global amphipod goals, values are the indices of the correct side room positions for key amphipod
amphipod_goals = { 'A': [29, 42], 'B': [31, 44], 'C': [33, 46], 'D': [35, 48] }
# global hallway indices 14-24 inclusive
hallway = range(14, 25)

def dfs_move(spot_index, amphipod, start_index, a_map, seen, start=False):
  if spot_index in seen: # Prevent infinite DFS by returning when visiting a spot already evaluated
    return []
  seen.append(spot_index) # add spot_index to seen list
  if start == True: # We don't want to evaluate the start position
    pass
  elif a_map[spot_index] != '.': # return when we reach a non-empty space
    return []

  moves = []
  # empty space found not directly outside a room
  if a_map[spot_index] == '.' and spot_index not in forbidden_moves:
    back_of_side_room_index = amphipod_goals[amphipod][1]
    # always allow move to the back of the side room if its possible to path there
    if spot_index == back_of_side_room_index:
      moves.append(spot_index)
    # allow move to index 0 of amphipod_goals, the front of the side room, if the back is filled with the same type of amphipod but not this one
    elif spot_index == amphipod_goals[amphipod][0]:
      # Need to stop infinite loop moving from back to front of side room
      # e.g. 1 of the amber amphipods, A1, paths to the empty space at the front of the first side room.
      # For this to be a valid move:
      #   1. A1 must not be at the back of the first side room
      #   2. A2 must be at the back of the first side room
      if a_map[back_of_side_room_index] == amphipod and start_index != back_of_side_room_index:
        moves.append(spot_index)
    # all amphipods starting in the hallway have already moved and cannot move unless into their destination.
    # Otherwise only allowing moves into the hallway from side rooms
    elif start_index not in hallway and spot_index in hallway:
      moves.append(spot_index)

  for move in dfs_move(spot_index + 13, amphipod, start_index, a_map, seen): # down
    moves.append(move)
  for move in dfs_move(spot_index - 13, amphipod, start_index, a_map, seen): # up
    moves.append(move)
  for move in dfs_move(spot_index + 1, amphipod, start_index, a_map, seen): # right
    moves.append(move)
  for move in dfs_move(spot_index - 1, amphipod, start_index, a_map, seen): # left
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
  move_counter = 0
  old_row = old_index // 13
  old_col = old_index % 13
  new_row = new_index // 13
  new_col = new_index % 13
  # Going from side room into side room
  if old_index not in hallway and new_index not in hallway:
    move_counter += (old_row - 1) + (new_row - 1) # 2 vertical moves: side room to hallway + hallway to side room. The 1 is the hallway row
    move_counter += abs(old_col - new_col) # horizontally in the hallway
  # Going from hallway into side room and side room into hallway
  else:
    # any combination of:
    move_counter += abs(old_row - new_row) # up/down
    move_counter += abs(old_col - new_col) # left/right
  return move_counter * energy_cost_per_move

def create_new_state(str_amphipod_map, old_index, new_index):
  l = list(str_amphipod_map) # convert to list
  l[old_index], l[new_index] = l[new_index], l[old_index]  # swap values at indices
  return "".join(l) # return as a string

def get_all_valid_moves(amphipod_map):
  moves = []
  for spot_index in range(len(amphipod_map)):
    if amphipod_map[spot_index].isalpha():# alphabetical test, ABCD amphipods
      amphipod = amphipod_map[spot_index]
      for move in dfs_move(spot_index, amphipod, spot_index, amphipod_map, [], True): # can return empty list if no valid moves
        new_index = move
        # create new string by swapping the old with new index to simulate a move, we only ever move amphipod to empty space '.' 
        new_state = create_new_state(amphipod_map, spot_index, new_index)
        # bundle the energy cost of the move and the new state, then append tuple to moves list
        moves.append((get_energy_cost(amphipod, spot_index, new_index), new_state))
  return moves

def main():
  puzzle_input  = "".join([line.replace("\n", "") for line in open('input.txt').readlines()])
  # representing the map as a string, to traverse rows +/- 13 to index, to traverse columns +/- 1 to index
  start = puzzle_input
  end = '##############...........####A#B#C#D###  #A#B#C#D#    #########  '

  visited = set() # Storing visited nodes in a set to prevent infinite evaluation

  queue = [(0, start)] # Initial node

  last = {} # last dict: key is the node in question, value is updated to be the previous node when following path of least cost

  # creates a defaultdict with default value (tentative energy value) as infinity for all nodes except {start: 0}, the energy cost of the initial state is zero
  min_energy_cost = defaultdict(lambda: float("inf"), {start: 0})

  while queue:

    node = heappop(queue) # get node with lowest energy cost

    cumulative_energy, state = node # unpack tuple

    if state == end: # if state represents the end game state
      current = state
      node_path = [current]
      while current in last: # Traverse backwards through last and prints the node path taken
        current = last[current]
        node_path.append(current)
      print("Node path:")
      for i in range(len(node_path) - 1, -1, -1):
        for j in range(len(node_path[i])):
          print(node_path[i][j], end="")
          if (j + 1) % 13 == 0 and j != 0:
            print("")
        print("")
      print("part1:", cumulative_energy) # the least energy required to organize the amphipods
      return

    visited.add(state)

    next_states = get_all_valid_moves(state)
    # get_all_valid moves should return a list of tuples that represents all valid next states from this state
    # each tuple consists of:
    #   first argument energy cost of going from old to new state
    #   second argument the new state as a string

    for next_state in next_states: # can reach dead end if no next states, the next node from the queue will then be evaluated
      energy_cost, state_map = next_state
      if state_map in visited: # Don't repeat evaluated nodes
        continue
      new_energy_cost = cumulative_energy + energy_cost
      if new_energy_cost < min_energy_cost[state_map]: # Found new min cost from start going through node to neighbour node
        last[state_map] = state # update last
        min_energy_cost[state_map] = new_energy_cost # update cost from start to this node
        heappush(queue, (new_energy_cost, state_map)) # push to queue to be evaluated

  print("unsolvable") # if the queue empties then the problem is unsolvable

if __name__ == '__main__':
  main()