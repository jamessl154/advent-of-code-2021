puzzle_input = [x for x in open("input.txt").read().split("\n")]

# print(puzzle_input)

class Octopus():

    def __init__(self, energy):
        self.energy = energy
        self.flashed = False
        self.adjacent_octopi = []

    def increase_energy(self):
        self.energy += 1

# Initialize cave and octopi energy
cave = []

for i in range(len(puzzle_input)):

    cave.append([])

    for j in range(len(puzzle_input[i])):

        octopus = Octopus(int(puzzle_input[i][j]))

        cave[i].append(octopus)

# Add adjacent octopi
for i in range(len(cave)):
    for j in range(len(cave[i])):

        a = cave[i][j]

        # left up
        if i - 1 >= 0 and j - 1 >= 0:
            a.adjacent_octopi.append(cave[i-1][j-1])
        # up
        if i - 1 >= 0:
            a.adjacent_octopi.append(cave[i-1][j])
        # right up
        if i - 1 >= 0 and j + 1 < len(cave[i]):
            a.adjacent_octopi.append(cave[i-1][j+1])
        # right
        if j + 1 < len(cave[i]):
            a.adjacent_octopi.append(cave[i][j+1])
        # right down
        if j + 1 < len(cave[i]) and i + 1 < len(cave):
            a.adjacent_octopi.append(cave[i+1][j+1])
        # down
        if i + 1 < len(cave):
            a.adjacent_octopi.append(cave[i+1][j])
        # left down
        if j - 1 >= 0 and i + 1 < len(cave):
            a.adjacent_octopi.append(cave[i+1][j-1])
        # left
        if j - 1 >= 0:
            a.adjacent_octopi.append(cave[i][j-1])

i = 1

while True:

    flash_counter = 0

    for a in cave:
        for b in a:
            b.flashed = False
            b.increase_energy()
    
    q = []

    for a in cave:
        for b in a:
            if b.energy > 9:
                b.flashed = True
                flash_counter += 1
                b.energy = 0
                q.append(b)
                while q:
                    n = q.pop(0)
                    for c in n.adjacent_octopi:
                        if c.flashed == False:
                            c.increase_energy()
                            if c.energy > 9:
                                c.flashed = True
                                flash_counter += 1
                                c.energy = 0
                                q.append(c)
    
    if flash_counter == 100:
        break

    i += 1

print(i)