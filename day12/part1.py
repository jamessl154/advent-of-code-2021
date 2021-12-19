puzzle_input = [x for x in open("input.txt").read().split("\n")]

# print(puzzle_input)

class Cave:
    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.connected_caves = []

    def add_connected_cave(self, Cave):
        self.connected_caves.append(Cave)

map = {}

def get_size(string):
    if string.islower():
        return "small"
    else:
        return "big"

for i in puzzle_input:
    n = i.split("-")
    if n[0] not in map:
        map[n[0]] = Cave(n[0], get_size(n[0]))
    if n[1] not in map:
        map[n[1]] = Cave(n[1], get_size(n[1]))

    map[n[0]].add_connected_cave(map[n[1]])
    map[n[1]].add_connected_cave(map[n[0]])

# for i in map["yw"].connected_caves:
#     print(i.name)

counter = 0

# https://everything.explained.today/Side_effect_(computer_science)/
# parameters are passed by reference in python so must make a copy
# for each recursive call to stop causing the side-effect of modifying
# the mutable argument passed by reference which is temp here

def dfs(cave, path, temp = []):
    global counter

    small_caves = temp.copy()
    cave_path = path.copy()
    cave_path.append(cave.name)

    if cave.name == "end":
        counter += 1
        print(cave_path)
        return

    if cave.size == "small":
        small_caves.append(cave)

    for i in cave.connected_caves:
        if i not in small_caves:
            dfs(i, cave_path, small_caves)

dfs(map["start"], [])

print(counter)