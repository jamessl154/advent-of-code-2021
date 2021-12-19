from collections import defaultdict

puzzle_input = [x for x in open("test.txt").read().split("\n")]

# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

# Help from: https://github.com/DenverCoder1/Advent-of-Code-2021/blob/main/Day-12/part2.py#L95-L111

graph = defaultdict(list)

visited = set()

for i in puzzle_input:
    a, b = i.split("-")
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, visited, visited_single_small_twice, path):

    path_copy = path.copy()
    path_copy.append(node)

    if node == "end":
        print(path_copy)
        return 1

    counter = 0

    for i in graph[node]:
        # Big caves or non-visited small caves
        if not i.islower() or i not in visited:
            # passing return value of set union as visited param
            counter += dfs(i, visited | {i}, visited_single_small_twice, path_copy)
        # Can visit one small cave that isnt start or end twice
        elif not visited_single_small_twice and i not in {"start", "end"}:
            counter += dfs(i, visited | {i}, True, path_copy)
    return counter

print(dfs("start", {"start"}, False, []))