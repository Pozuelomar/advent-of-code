import sys
import numpy as np

pipes = np.array([list(l) for l in sys.stdin.read().splitlines()])
pipes2 = np.full(pipes.shape + np.array([2, 2]), ".")
pipes2[1:-1, 1:-1] = pipes
pipes = pipes2
print(pipes)

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
    "S": {D: R, L: U},  # Works only in this dataset
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


visited = set()
sys.setrecursionlimit(100000)


# # Test with pipes blocking water on the entire square
# def foo(pos):
#     # print(pos)
#     if not -1 <= pos[0] < pipes.shape[0] + 1:
#         return
#     if not -1 <= pos[1] < pipes.shape[1] + 1:
#         return
#     if tuple(pos) in visited:
#         return
#     if tuple(pos) in loop_pipes:
#         return
#     visited.add(tuple(pos))
#     for direction in [U, D, L, R]:
#         direction = np.array(direction)
#         foo(pos + direction)

# Shifted index map
# Water flowing in 0, should have the position of F + [.5,.5]
# But we use the same position as F to have round index
# F 7
#  0
# L J


# Using pipes as barriers
def foo(pos):
    # print(pos)
    if not 0 <= pos[0] < pipes.shape[0] - 1:
        return
    if not 0 <= pos[1] < pipes.shape[1] - 1:
        return
    if tuple(pos) in visited:
        return
    visited.add(tuple(pos))
    for direction in [U, D, L, R]:
        match direction:
            case (-1, 0):  # U
                if (
                    tuple(pos) in loop_pipes
                    and tuple(pos + R) in loop_pipes
                    and L in directions[pipes[*pos]]
                    and R in directions[pipes[*pos + R]]
                ):
                    continue
            case (1, 0):  # D
                if (
                    tuple(pos + D) in loop_pipes
                    and tuple(pos + D + R) in loop_pipes
                    and L in directions[pipes[*pos + D]]
                    and R in directions[pipes[*pos + D + R]]
                ):
                    continue
            case (0, -1):  # L
                if (
                    tuple(pos) in loop_pipes
                    and tuple(pos + D) in loop_pipes
                    and U in directions[pipes[*pos]]
                    and D in directions[pipes[*pos + D]]
                ):
                    continue
            case (0, 1):  # R
                if (
                    tuple(pos + R) in loop_pipes
                    and tuple(pos + R + D) in loop_pipes
                    and U in directions[pipes[*pos + R]]
                    and D in directions[pipes[*pos + R + D]]
                ):
                    continue
        direction = np.array(direction)
        foo(pos + direction)


foo(np.array([0, 0]))
print(len(visited))


# Print pipe loop
for i in range(pipes.shape[0] - 1):
    for j in range(pipes.shape[1] - 1):
        if (i, j) in loop_pipes:
            print(pipes[i, j], end="")
        else:
            print(" ", end="")
    print()

# Print water
for i in range(pipes.shape[0] - 1):
    for j in range(pipes.shape[1] - 1):
        if (i, j) in visited:
            print(".", end="")
        else:
            print(" ", end="")
    print()


# Full print pipe loop and water
for i in range(pipes.shape[0] - 1):
    for j in range(pipes.shape[1] - 1):
        if (i, j) in loop_pipes:
            print(pipes[i, j] + " ", end="")
        else:
            print("  ", end="")
    print()
    print(" ", end="")
    for j in range(pipes.shape[1] - 1):
        if (i, j) in visited:
            print(". ", end="")
        else:
            print("  ", end="")
    print()

# Looking for dry area with no pipe
total = 0
for i in range(pipes.shape[0]):
    for j in range(pipes.shape[1]):
        if (i, j) in loop_pipes:
            continue
        if (i - 1, j - 1) in visited:
            continue
        if (i, j - 1) in visited:
            continue
        if (i - 1, j) in visited:
            continue
        if (i, j) in visited:
            continue
        total += 1
print(total)
# 453
