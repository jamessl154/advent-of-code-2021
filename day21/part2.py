from itertools import product
from functools import lru_cache

#  Solution from: https://github.com/mebeim/aoc/blob/master/2021/README.md#day-21---dirac-dice

p1_pos = 5
p2_pos = 3

Quantum_rolls = []

# https://docs.python.org/3/library/itertools.html#itertools.product
for three_rolls in product(range(1,4), range(1,4), range(1,4)):
    Quantum_rolls.append(sum(three_rolls))

print(Quantum_rolls) # 27 permutations

# https://docs.python.org/3/library/functools.html#functools.lru_cache
@lru_cache(maxsize=None)
# The result of turn with the same state is memoized to prevent repeated evaluations
def turn(pos_A, score_A, pos_B, score_B):
    if score_A >= 21:
        return 1, 0

    if score_B >= 21:
        return 0, 1

    wins_A = wins_B = 0

    # Quantum rolls is just a list of the sum of 3 rolls of the quantum die.
    # https://www.mathsisfun.com/combinatorics/combinations-permutations.html
    # Each member is one universe or permutation with repetition of 1, 2, 3
    for roll in Quantum_rolls:

        # pA plays
        pos_new = (pos_A + roll) % 10
        score_new = score_A + pos_new + 1

        # pB plays, turn() called with swapped arguments and new state,
        # and recursively gets called until base case solved
        wins_B2, wins_A2 = turn(pos_B, score_B, pos_new, score_new)

        wins_A += wins_A2
        wins_B += wins_B2

    return wins_A, wins_B

print("part2", max(turn(p1_pos, 0, p2_pos, 0)))