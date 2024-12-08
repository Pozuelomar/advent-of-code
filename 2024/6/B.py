import sys

arr = []
for line in sys.stdin:
    arr.append(list(line.strip("\n")))

start = (0, 0)
for i in range(1, len(arr)):
    for j in range(1, len(arr[i])):
        if arr[i][j] == "^":
            start = (i, j)
            break


def loops(arr):
    position = start
    direction = (-1, 0)  # up
    position_set = {(start, direction)}

    next_position = (position[0] + direction[0], position[1] + direction[1])
    while 0 <= next_position[0] < len(arr) and 0 <= next_position[1] < len(arr[0]):
        if arr[next_position[0]][next_position[1]] == "#":
            direction = (direction[1], -direction[0])
        else:
            position = next_position

        if (position, direction) in position_set:
            return 1
        position_set.add((position, direction))
        next_position = (position[0] + direction[0], position[1] + direction[1])
    return 0


s = 0
for i in range(130):
    for j in range(130):
        if arr[i][j] != ".":
            continue
        arr[i][j] = "#"
        s += loops(arr)
        arr[i][j] = "."

print(s)
