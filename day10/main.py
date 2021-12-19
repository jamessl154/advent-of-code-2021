puzzle_input = [x for x in open("input.txt").read().split("\n")]

# print(puzzle_input)

class Counter:

    def __init__(self):
        self.counter = 0

    def add_count(self, char):
        if char == ")":
            self.counter += 3
        if char == "]":
            self.counter += 57
        if char == "}":
            self.counter += 1197
        if char == ">":
            self.counter += 25137

count_list = []

for line in puzzle_input:

    # print(line)

    stack = []

    line_count = Counter()

    for char in line:
        if char == "[":
            stack.append("]")
        if char == "(":
            stack.append(")")
        if char == "{":
            stack.append("}")
        if char == "<":
            stack.append(">")

        if char == "]":
            if stack.pop() != "]":
                line_count.add_count("]")
        if char == ")":
            if stack.pop() != ")":
                line_count.add_count(")")
        if char == "}":
            if stack.pop() != "}":
                line_count.add_count("}")
        if char == ">":
            if stack.pop() != ">":
                line_count.add_count(">")

    if line_count.counter == 0:

        # print(stack)
        
        count = 0

        while stack:

            count = count * 5

            char = stack.pop()

            if (char == ")"):
                count += 1
            if (char == "]"):
                count += 2
            if (char == "}"):
                count += 3
            if (char == ">"):
                count += 4
        
        count_list.append(count)

# print(count_list)

count_list = sorted(count_list)

# print(count_list)

mid = len(count_list) // 2

print(count_list[mid])