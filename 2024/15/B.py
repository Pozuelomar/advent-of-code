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
        warehouse.append([])
        for c in line.strip():
            match c:
                case "#":
                    warehouse[-1].extend(["#", "#"])
                case "@":
                    warehouse[-1].extend(["@", "."])
                case ".":
                    warehouse[-1].extend([".", "."])
                case "O":
                    warehouse[-1].extend(["[", "]"])

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


def can_move(x, y, direction):
    new_x, new_y = x + direction[0], y + direction[1]
    match warehouse[new_x][new_y]:
        case ".":
            return True
        case "#":
            return False
        case "[":
            boxes = [(new_x, new_y), (new_x, new_y + 1)]
        case "]":
            boxes = [(new_x, new_y - 1), (new_x, new_y)]

    if direction == (0, -1):
        return can_move(*boxes[0], direction)
    if direction == (0, 1):
        return can_move(*boxes[1], direction)
    for box in boxes:

        # Can create diamond-shape recursions leading to exponential time complexity
        if not can_move(*box, direction):
            return False
    return True


def move(x, y, direction):
    new_x, new_y = x + direction[0], y + direction[1]
    match warehouse[new_x][new_y]:
        case ".":
            return
        case "#":
            return
        case "[":
            boxes = [(new_x, new_y), (new_x, new_y + 1)]
        case "]":
            boxes = [(new_x, new_y - 1), (new_x, new_y)]

    if direction == (0, -1):
        move(*boxes[0], direction)
    elif direction == (0, 1):
        move(*boxes[1], direction)
    else:
        for box in boxes:
            move(*box, direction)
    for box in boxes:
        warehouse[box[0]][box[1]] = "."
    warehouse[boxes[0][0] + direction[0]][boxes[0][1] + direction[1]] = "["
    warehouse[boxes[1][0] + direction[0]][boxes[1][1] + direction[1]] = "]"


for action in actions:
    if can_move(x, y, directions[action]):
        move(x, y, directions[action])
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
        if warehouse[i][j] == "[":
            s += i * 100 + j
print(s)
