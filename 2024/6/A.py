import sys

arr = []
for line in sys.stdin:
    arr.append(line.strip("\n"))

position = (0, 0)
for i in range(1, len(arr)):
    for j in range(1, len(arr[i])):
        if arr[i][j] == "^":
            position = (i, j)
            break

direction = (-1, 0)  # up
position_set = {position}

next_position = (position[0] + direction[0], position[1] + direction[1])
while 0 <= next_position[0] < len(arr) and 0 <= next_position[1] < len(arr[0]):
    if arr[next_position[0]][next_position[1]] == "#":
        direction = (direction[1], -direction[0])
    else:
        position = next_position

    position_set.add(position)
    next_position = (position[0] + direction[0], position[1] + direction[1])


# for i in range(130):
#     for j in range(130):
#         if (i, j) in position_set:
#             print("+", end="")
#         elif arr[i][j] == "#":
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

print(len(position_set))
