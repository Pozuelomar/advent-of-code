import sys
import numpy as np

pipes = np.array([list(l) for l in sys.stdin.read().splitlines()])
# # Surrounding pipes with empty space for easier processing
# pipes2 = np.full(pipes.shape + np.array([2, 2]), ".")
# pipes2[1:-1, 1:-1] = pipes
# pipes = pipes2
# print(pipes)

D = (1, 0)
U = (-1, 0)
L = (0, -1)
R = (0, 1)
directions = {
    "|": {D: D, U: U},
    "-": {R: R, L: L},
    "F": {U: R, L: D},
    "7": {U: L, R: D},
    "J": {D: L, R: U},
    "L": {D: R, L: U},
    "S": {D: R, L: U},  # Works only in this dataset as S=L
    ".": {},
}

start = np.array(np.where(pipes == "S"))[:, 0]

for direction in [U, D, L, R]:
    direction = np.array(direction)
    position = start + direction
    if tuple(direction) in directions[pipes[*position]]:
        break

loop_pipes = set()
loop_pipes.add(tuple(position))
while pipes[*position] != "S":
    direction = directions[pipes[*position]][tuple(direction)]
    position += direction
    loop_pipes.add(tuple(position))

# print(loop_pipes)


# # Flooding the area, to count the remaining dry spots

# flooded = set()
# sys.setrecursionlimit(100000)


# # # Test with pipes blocking water on the entire square
# # def foo(pos):
# #     # print(pos)
# #     if not -1 <= pos[0] < pipes.shape[0] + 1:
# #         return
# #     if not -1 <= pos[1] < pipes.shape[1] + 1:
# #         return
# #     if tuple(pos) in flooded:
# #         return
# #     if tuple(pos) in loop_pipes:
# #         return
# #     flooded.add(tuple(pos))
# #     for direction in [U, D, L, R]:
# #         direction = np.array(direction)
# #         foo(pos + direction)

# # Shifting index map
# # Water flowing in 0 is shifted diagonally by half a cell.
# # 0 have physical position of F + [.5,.5]
# # but we use the same coordinates as F to have round index
# # F 7
# #  0
# # L J


# # Using pipes as barriers
# def flood(pos):
#     if not 0 <= pos[0] < pipes.shape[0]:
#         return
#     if not 0 <= pos[1] < pipes.shape[1]:
#         return
#     if tuple(pos) in flooded:
#         return
#     flooded.add(tuple(pos))

#     for direction in [U, D, L, R]:
#         match direction:
#             case (-1, 0):  # U
#                 pos1 = pos
#                 pos2 = pos + R
#                 d1 = L
#                 d2 = R
#             case (1, 0):  # D
#                 pos1 = pos + D
#                 pos2 = pos + D + R
#                 d1 = L
#                 d2 = R
#             case (0, -1):  # L
#                 pos1 = pos
#                 pos2 = pos + D
#                 d1 = U
#                 d2 = D
#             case (0, 1):  # R
#                 pos1 = pos + R
#                 pos2 = pos + R + D
#                 d1 = U
#                 d2 = D
#         if (  # Two pipes from the loop are connected, blocking water from pos to pos+direction
#             tuple(pos1) in loop_pipes
#             and tuple(pos2) in loop_pipes
#             and d1 in directions[pipes[*pos1]]
#             and d2 in directions[pipes[*pos2]]
#         ):
#             continue
#         direction = np.array(direction)
#         flood(pos + direction)


# flood(np.array([0, 0]))

# # better_print = {
# #     "|": "║",
# #     "-": "═",
# #     "F": "╔",
# #     "7": "╗",
# #     "J": "╝",
# #     "L": "╚",
# #     "S": "╚",
# # }
# # # Print pipe loop
# # for i in range(pipes.shape[0] - 1):
# #     for j in range(pipes.shape[1] - 1):
# #         if (i, j) in loop_pipes:
# #             print(better_print[pipes[i, j]], end="")
# #         else:
# #             print(" ", end="")
# #     print()

# # # Print water
# # for i in range(pipes.shape[0] - 1):
# #     for j in range(pipes.shape[1] - 1):
# #         if (i, j) in flooded:
# #             print(".", end="")
# #         else:
# #             print(" ", end="")
# #     print()


# # # Full print pipe loop and water
# # for i in range(pipes.shape[0] - 1):
# #     for j in range(pipes.shape[1] - 1):
# #         if (i, j) in loop_pipes:
# #             print(better_print[pipes[i, j]], end="")
# #         else:
# #             print("x", end="")
# #         if (
# #             (i, j) in loop_pipes
# #             and (i, j + 1) in loop_pipes
# #             and L in directions[pipes[i, j]]
# #             and R in directions[pipes[i, j + 1]]
# #         ):
# #             print("═", end="")
# #         else:
# #             print(" ", end="")
# #     print()
# #     print(" ", end="")
# #     for j in range(pipes.shape[1] - 1):
# #         if (i, j) in flooded:
# #             print(".", end="")
# #         else:
# #             print(" ", end="")
# #         if (
# #             (i, j + 1) in loop_pipes
# #             and (i + 1, j + 1) in loop_pipes
# #             and U in directions[pipes[i, j + 1]]
# #             and D in directions[pipes[i + 1, j + 1]]
# #         ):
# #             print("║", end="")
# #         else:
# #             print(" ", end="")
# #     print()

# # Looking for dry areas
# total = 0
# for i in range(pipes.shape[0]):
#     for j in range(pipes.shape[1]):
#         if any(
#             map(flooded.__contains__, [(i - 1, j - 1), (i, j - 1), (i - 1, j), (i, j)])
#         ):
#             continue
#         total += 1
# print(total)
# # 453


# Xray method
from operator import xor
from itertools import accumulate

total = sum(
    a & b & c
    for i, l in enumerate(pipes)
    for a, b, c in zip(
        accumulate(
            [(i, j) in loop_pipes and D in directions[v] for j, v in enumerate(l)],
            xor,
        ),
        accumulate(
            [(i, j) in loop_pipes and U in directions[v] for j, v in enumerate(l)],
            xor,
        ),
        [(i, j) not in loop_pipes for j, _ in enumerate(l)],
    )
)
print(total)
# 453
