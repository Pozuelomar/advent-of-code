import sys
import numpy as np

pipes = np.array([list(l) for l in sys.stdin.read().splitlines()])

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
}

start = np.array(np.where(pipes == "S"))[:, 0]

for direction in [U, D, L, R]:
    position = start + np.array(direction)
    if direction in directions[pipes[*position]]:
        break

i = 1
while pipes[*position] != "S":
    direction = directions[pipes[*position]][tuple(direction)]
    position += direction
    i += 1
print(i // 2)
# 6890
