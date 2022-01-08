from re import split

# Solution from: https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hqxczc4/?utm_source=share&utm_medium=web2x&context=3
# Code: https://topaz.github.io/paste/#XQAAAQDTBAAAAAAAAAAxnUhop0JRHqF7STMJ21b5rjzfpDJwgkC8Ju0TgQ6JC3kWm9UKWfjP+KPMGQ04ShwJz/XAH/ZDwwkLtPIVaIWX+xHCdFYDdj1AbGvdpkhagrBjAbxncP3KGQMw6x8dN+Fhc9XmNKkwlmXQMk14LaklWNpRO0LfDVwdlp1eXQxgvKedpeidchA0tcLwSC0HpyC6e61EWmfMXh6+HjYND61l/Zob5BfKrhOnNG0tj1kCEPdw4ML5NoR7GFmmASpjpjTHsD0jpExCpkNwjo02kn30u2dqA8d/jwAD3klLDt8uRF3WF1Duwkx16yJXSgLXgwjd2mO78KtKpVg3jSsuH3V7tVViHugCdExntqSfnzg89R51oGqiZ6heNtDPOUq0APaBYNoXkoBz8T7IOxVdFm5FevG+tnCTFopLiOEfUVCC9duFZGETAD+qxVDXoO1xjDtqRogyvR6dcU5xWSPVie1kd/i9YRUvdWtnnBzB11gKjRG0NRfWAnYFn1ooX7tKxzAN83bGz+KGKPX5bDdae5Dru/gQKXMV8zPicitXIbIOXrTJP0VV4azJ9xHQN9qEAguMjvBfYn9g5gg5VdQMgK+p1WLDCp2okwUq6A11igItQMttxNnVZWqh0czTTiQlvj3Jj/EBr6mpxzMdlbzhrWNHGE+0r7rIzVF2ejBC0rfkUS19kMKf2gRVXKDsru+pGAryhRSCGM97mtgHANmcNzILv9A6TNcVcjR/fdTEs9UFtB/ghWy4pf6Bv2twvyVkVIYsSvK4JCFlmuL2f7+YDjBqzm17Cv/zjG6g

with open("input.txt", "r") as f:
  puzzle_input = f.read().splitlines()

puzzle_input = [
character
.replace('on', '1')
.replace('off', '0')
.replace('x=', '')
.replace(',y=', ' ')
.replace(',z=', ' ')
.replace('..', ' ')
for character in puzzle_input]

puzzle_input = [[int(character) for character in string.split(' ')] for string in puzzle_input]

# cuboids in puzzle_input become: [0/+1/-1, x_min, x_max, y_min, y_max, z_min, z_max]
# cuboids[0]: +1 addition cuboid, -1 subtraction cuboid, 0 cuboid off step

# Find intersection cuboid of 2 cuboids s and t, and whether it is a subtraction or addition cuboid
def intersection(s, t):
  # List of function objects that we call with the 2 cuboids s and t
  mm = [lambda a, b: -b, max, min, max, min, max, min]

  # i in mm[i] tells us which function to apply to the arguments (s[i], t[i])
  # so that n becomes the cuboid intersection between s and t
  n = [mm[i](s[i], t[i]) for i in range(7)]
  # n[0] is calculated using the inclusion-exclusion principle: https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
  # To find the area of 2 overlapping cuboids, add their areas and subtract the intersection
  # My understanding: For the nth overlap the intersection is multiplied by -1^n to prevent double counting
  # So if a cuboid in our map is a subtract cuboid, the intersection of cuboids that overlap it should be
  # addition cuboids and vice versa

  # Bounds checking, only return valid cuboid intersections
  return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n

# cuboid map
cores = []

# for each reboot cuboid step
for cuboid in puzzle_input:
  # 'off' cuboids do not exist, only their intersections matter
  to_add = [cuboid] if cuboid[0] == 1 else []

  # for each cuboid existing in our map
  for core in cores:
    inter = intersection(cuboid, core)
    # valid cuboid intersections return non-None
    if inter:
      to_add += [inter]

  # Add all intersection cuboids with existing cuboids in the map
  # + initial cuboid step (only if 'on')
  cores += to_add

def countoncubes(cores):
  oncount = 0
  for c in cores:
    # calculate all areas of cuboids, both subtraction and addition, to get non-double-counted result
    oncount += c[0] * (c[2]-c[1]+1) * (c[4]-c[3]+1) * (c[6]-c[5]+1)
  return oncount

print('part2', countoncubes(cores))