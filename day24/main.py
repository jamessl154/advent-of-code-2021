# Help from: https://github.com/mebeim/aoc/blob/master/2021/README.md#day-24---arithmetic-logic-unit

def get_constraints(puzzle_input):
  # divides input into 14 steps 18 lines each, 7 push and pop steps each
  # returns a list of constraints that we must fulfil to get z equal to 0 at the last step
  stack = []
  constraints = []

  # 18 line steps
  i = 0; j = 18; step_number = 0
  while j < len(puzzle_input) + 1:
    step = puzzle_input[i:j]

    if step[4][2] == 1: # push
      stack.append((step_number, step[15][2])) # first constant
    elif step[4][2] == 26: # pop
      second_constant = step[5][2]
      popped_step_num, first_constant = stack.pop() # latest push step
      constraints.append((step_number, popped_step_num, first_constant + second_constant))
      # push_digit + A + B == pop_digit
    i += 18
    j += 18
    step_number += 1

  return constraints

def get_max(constraints):
  input_digits = [0] * 14

  for pop_step_index, push_step_index, diff in constraints: # push_digit + D == pop_digit, to maximise one digit should always be 9
    if diff > 0: # The highest that we can set the push_digit is 9 - diff when diff > 0 to get a pop_digit in range 1-9
        input_digits[pop_step_index], input_digits[push_step_index] = 9, 9 - diff
    else: # when diff < 0 we are maximising by setting push_digit to 9 and pop_digit to the result 9 + D
        input_digits[pop_step_index], input_digits[push_step_index] = 9 + diff, 9

  return int("".join(map(str, input_digits)))

def get_min(constraints):
  input_digits = [0] * 14

  for pop_step_index, push_step_index, diff in constraints: # to minimise, one digit should always be 1
    if diff > 0: # minimising by setting push_step_index to 1, pop_digit becomes the result of 1 + diff
      input_digits[pop_step_index], input_digits[push_step_index] = 1 + diff, 1
    else: # The lowest that we can set the push_digit is 1 - diff when diff <= 0 to get a pop_digit in range 1-9
      input_digits[pop_step_index], input_digits[push_step_index] = 1, 1 - diff

  return int("".join(map(str, input_digits)))

def main():
  puzzle_input = [line.split() for line in open("input.txt")]
  for line in puzzle_input:
    if len(line) == 3 and not line[2].isalpha(): # short circuit and
      line[2] = int(line[2])

  constraints = get_constraints(puzzle_input)
  max_num = get_max(constraints)
  print("part1", max_num)
  min_num = get_min(constraints)
  print("part2", min_num)

if __name__ == "__main__":
  main()