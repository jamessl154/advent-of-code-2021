min_x = 57
max_x = 116
min_y = -198
max_y = -148

class Probe:
    def __init__(self, x_velocity, y_velocity):
        self.x = 0
        self.y = 0

        # record of the probes initial velocities
        self.initial_velocity_tuple = (x_velocity, y_velocity)

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def step(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

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

# We can see from the example that natural limits for starting x_velocity and y_velocity are max_y and max_x
# This makes sense because if you throw any faster in either axis, you will miss the target in one step
# From part 1 we have the upward y limit of 197
# x is strictly positive, impossible to hit target when throwing straight up or backwards

result = set()

# Brute force count unique initial velocity pairs
for i in range(117):
    for j in range(-198, 198):

        probe = Probe(i, j)

        while True:
            if target_missed(probe):
                break
            if target_hit(probe):
                result.add(probe.initial_velocity_tuple)
                break
            probe.step()

print(len(result))