import sys
from math import lcm

directions = sys.stdin.readline().strip()
sys.stdin.readline()
map = {line[:3]: (line[7:10], line[12:15]) for line in sys.stdin}

# print(map)
start_areas = [area for area in map if area.endswith("A")]

# # Graph analysis
# for area in start_areas:
#     steps = 0
#     seen = {}
#     print()
#     print('new area', area)
#     while 1:
#         if (area, steps % len(directions)) in seen:
#             print('seen', (area, steps % len(directions)), 'at', seen[(area, steps % len(directions))])
#             print('again at', steps)
#             print('loop length', steps - seen[(area, steps % len(directions))])
#             break

#         seen[(area, steps % len(directions))] = steps
#         if area.endswith('Z'):
#             print('Z',steps)
#         area = map[area][directions[steps % len(directions)] == 'R']
#         steps += 1

# Analysis showed that:
#   1. all start_areas loop back, and countain exacly 1 Z per loop.
#   2. the Z is virtually in the same position in the loop as the A, this is key to resolve the problem.
#      (if the loop starts at index 5 with length 1000 (looping at 1005), the Z will be at index 1000, 5 before teh know, like thh start)
# Said otherwise, the index of the only Z we are gonna encounter, is equal to the length of the loop.
# any_Z = first_Z + N * length_of_loop
# any_Z = first_Z + N * first_Z
# any_Z = N+ * first_Z
# This means the all positions of Z are multiple of the index the first one (= the length of the loop).

# S -> K - -> - |
#      |        |
#      Z - <- - -

first_Zs = []
for area in start_areas:
    steps = 0
    while not area.endswith("Z"):
        area = map[area][directions[steps % len(directions)] == "R"]
        steps += 1
    first_Zs.append(steps)

print(first_Zs)

print(lcm(*first_Zs))
# 12315788159977
