puzzle_input = [int(x) for x in open("input.txt").read().strip().split(",")]

sum = 0

for i in puzzle_input:
    sum += i

mean = sum // len(puzzle_input)

def fuel_cost(position):

    fuel = 0

    for i in puzzle_input:
        move_cost = abs(i - position)
        
        fuel += move_cost
    
    return fuel

record = fuel_cost(mean)

above = mean + 1
below = mean - 1

while fuel_cost(below) < record:
    record = min(fuel_cost(below), record)
    below -= 1

while fuel_cost(above) < record:
    record = min(fuel_cost(above), record)
    above += 1

print(record)