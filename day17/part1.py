min_x = 57
max_x = 116
min_y = -198
max_y = -148

class Probe:
    def __init__(self, x_velocity, y_velocity):
        self.x = 0
        self.y = 0
        self.record_y = 0
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def step(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.record_y = max(self.record_y, self.y)

        # Drag
        if self.x_velocity > 0:
            self.x_velocity -= 1
        elif self.x_velocity < 0:
            self.x_velocity += 1

        # Gravity
        self.y_velocity -= 1

def target_missed(probe):
    if probe.x > max_x or probe.y < min_y:
        return True
    else:
        return False

def target_hit(probe):
    if probe.x in range(min_x, max_x + 1) and probe.y in range(min_y, max_y + 1):
        return True
    else:
        return False

# Throwing at this trajectory, x will reach its asymptote
# if we want the highest Y position
# pick an integer within range min_x, max_x

def decrement_sum(num):
    i = 0
    while num > 0:
        i += num
        num -= 1
    return i

# print(decrement_sum(10)) # 55 not in range 57-116
# print(decrement_sum(11)) # 66 is in range

# Found i by trial and error looking for the pattern
# any i below 197 is increasing, any i above is missing
i = 197
probe = Probe(11, i)

while True:
    probe.step()

    if target_missed(probe):
        print(probe.x, probe.y)
        break
    if target_hit(probe):
        print(probe.record_y)
        break