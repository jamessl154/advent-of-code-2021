def ALU(ALU_input,command_list):
  input_index,x,y,w,z = 0,0,0,0,0
  for command in command_list:
    match command[0]:
      case 'inp':
        w = ALU_input[input_index]
        input_index += 1
      case 'add':
        match command[1]:
          case 'x':
            x = eval(command[1]+"+"+command[2])
          case 'y':
            y = eval(command[1]+"+"+command[2])
          case 'z':
            z = eval(command[1]+"+"+command[2])
      case 'mul':
        if eval(command[1]) != 0:
          match command[1]:
            case 'x':
              x = eval(command[1]+"*"+command[2])
            case 'y':
              y = eval(command[1]+"*"+command[2])
            case 'z':
              z = eval(command[1]+"*"+command[2])
      case 'div':
        if eval(command[1]) != 0:
          match command[1]:
            case 'x':
                x = eval(command[1]+"//"+command[2])
            case 'y':
                y = eval(command[1]+"//"+command[2])
            case 'z':
                z = eval(command[1]+"//"+command[2])
      case 'mod':
        if eval(command[1]) != 0:
          match command[1]:
            case 'x':
              x = eval(command[1]+"%"+command[2])
            case 'y':
              y = eval(command[1]+"%"+command[2])
            case 'z':
              z = eval(command[1]+"%"+command[2])
      case 'eql':
        match command[1]:
          case 'x':
            x = 1 if eval(command[1]+"=="+command[2]) == True else False
          case 'y':
            y = 1 if eval(command[1]+"=="+command[2]) == True else False
          case 'z':
            z = 1 if eval(command[1]+"=="+command[2]) == True else False

  return 'valid' if z == 0 else 'invalid'

def contains_zero_digit(integer): # https://stackoverflow.com/a/3847776
  divisor = 10
  remainder = 0

  while divisor <= integer:
    new_remainder = integer % divisor

    if new_remainder - remainder == 0:
      return True

    divisor *= 10
    remainder = new_remainder
  return False

def main():
  puzzle_input = [line.split() for line in open("input.txt")]

  # check all combinations of 14 digit 0-9
  # from largest 99999999999999 containing no 0 digits

  ALU_input = 99999999999999

  while True:
    if not contains_zero_digit(ALU_input):
      # https://stackoverflow.com/a/51092473
      result = ALU(list(map(int, str(ALU_input))), puzzle_input)
      print(ALU_input, result)
      if result == 'valid':
        print("part1", ALU_input)
        return
    ALU_input -= 1

if __name__ == '__main__':
  main()