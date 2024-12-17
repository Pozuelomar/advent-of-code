import sys
import time

warehouse = []
actions = []
part = 1
for line in sys.stdin:
    if part == 1:
        if line == "\n":
            part = 2
            continue
        warehouse.append(list(line.strip()))

    if part == 2:
        actions.extend(list(line.strip()))

print(warehouse)
print(actions)


x, y = None, None
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "@":
            x, y = i, j
            warehouse[i][j] = "."

print(x, y)

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def try_move(x, y, direction):
    new_x, new_y = x + direction[0], y + direction[1]
    match warehouse[new_x][new_y]:
        case ".":
            return True
        case "#":
            return False
        case "O":
            if try_move(new_x, new_y, direction):
                warehouse[new_x][new_y] = "."
                warehouse[new_x + direction[0]][new_y + direction[1]] = "O"
                return True
            return False


for action in actions:
    if try_move(x, y, directions[action]):
        x, y = x + directions[action][0], y + directions[action][1]

    # s = []
    # for row in warehouse:
    #     s.append("".join(row))
    # print("\n".join(s))
    # print(action)
    # # 100 ms
    # time.sleep(0.01)

s = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "O":
            s += i * 100 + j
print(s)
