def move_sea_cucumbers(sea_cucumber_map, direction):
  swaps = []
  if direction == 'east':
    for row in range(len(sea_cucumber_map)):
      for col in range(len(sea_cucumber_map[row])):
        col_destination = col + 1 # Scouting destination
        if col == len(sea_cucumber_map[row]) - 1:
          col_destination = 0 # moves out of bounds wrap back onto the map
        if sea_cucumber_map[row][col] == '>' and sea_cucumber_map[row][col_destination] == '.': # empty space in destination
          swaps.append((row, col, col_destination, 'east'))
  elif direction == 'south':
    for row in range(len(sea_cucumber_map)):
      for col in range(len(sea_cucumber_map[row])):
        row_destination = row + 1 # Scouting destination
        if row == len(sea_cucumber_map) - 1:
          row_destination = 0 # moves out of bounds wrap back onto the map
        if sea_cucumber_map[row][col] == 'v' and sea_cucumber_map[row_destination][col] == '.': # empty space in destination
          swaps.append((row, col, row_destination, 'south'))
  # Move by swapping empty space with sea cucumber only after all scouting is done
  for row, col, dest, direction in swaps:
    if direction == 'east':
      sea_cucumber_map[row][dest], sea_cucumber_map[row][col] = sea_cucumber_map[row][col], sea_cucumber_map[row][dest]
    elif direction == 'south':
      sea_cucumber_map[dest][col], sea_cucumber_map[row][col] = sea_cucumber_map[row][col], sea_cucumber_map[dest][col]
  return (len(swaps), sea_cucumber_map)

def main():
  sea_cucumber_map = [list(line.strip()) for line in open("input.txt")]
  step_count = 0
  while True:
    current_step_moves = 0
    east_facing_herd_moves, sea_cucumber_map = move_sea_cucumbers(sea_cucumber_map, "east") # scout and move east herd first
    south_facing_herd_moves, sea_cucumber_map = move_sea_cucumbers(sea_cucumber_map, "south") # then scout and move south herd
    current_step_moves = east_facing_herd_moves + south_facing_herd_moves
    step_count += 1
    if current_step_moves == 0:
      break
  print("part1", step_count)

if __name__ == '__main__':
  main()