import sys

directions = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

corners = []
pos = (0, 0)
for line in sys.stdin:
    _, _, color = line.strip().split()
    dis, dir = color[2:-2], color[-2]
    dis = int(dis, 16)
    dir = "RDLU"[int(dir)]
    # print(dir, dis)
    corners.append(pos)
    pos = (pos[0] + directions[dir][0] * dis, pos[1] + directions[dir][1] * dis)

# print(corners)

# Doubling the coordinates
# We introduce extra collumns and lines between the original ones
# to take into account the variable sizes of the rectangles
# We use x_indexes and y_indexes to map the doubled coordinates to the original ones

# From this trenches we extract the coordinates of the corners
# ..#####.
# ..#...##
# ..#....#
# ###....#
# #......#
# #......#
# ########

# We expand in a coordinate system like this:
# x_indexes = [0,1,3,6], y_indexes = [0,2,6,7]
#   0 2 6 7
# 0 ..###..
#   ..#.#..
# 1 ..#.###
#   ..#...#
# 3 ###...#
#   #.....#
# 6 #######

# Which encodes the foolwing line widths:
#   1113101
# 1 ..###..
# 0 ..#.#..
# 1 ..#.###
# 1 ..#...#
# 1 ###...#
# 2 #.....#
# 1 #######

# We can then compute the area of each cell by multiplying the widths:
#   1113101
# 1 ..131..
# 0 ..000..
# 1 ..13101
# 1 ..13101
# 1 1113101
# 2 2226202
# 1 1113101

x_indexes = sorted(set(x for x, y in corners))
y_indexes = sorted(set(y for x, y in corners))
# for x in x_indexes:
#     for y in y_indexes:
#         if (x, y) in corners:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()

trench = set()
for (x1, y1), (x2, y2) in zip(corners, corners[1:] + corners[:1]):
    x1 = x_indexes.index(x1) * 2
    x2 = x_indexes.index(x2) * 2
    y1 = y_indexes.index(y1) * 2
    y2 = y_indexes.index(y2) * 2
    if x1 == x2:
        trench.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
    else:
        trench.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))

# print(trench)
# for x in range(len(x_indexes) * 2 - 1):
#     for y in range(len(y_indexes) * 2 - 1):
#         if (x, y) in trench:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()


flooded = set()

sys.setrecursionlimit(10000000)


def flood(x, y):
    if not (-1 <= x <= len(x_indexes) * 2 + 1 and -1 <= y <= len(y_indexes) * 2 + 1):
        return
    if (x, y) in trench:
        return
    if (x, y) in flooded:
        return
    flooded.add((x, y))
    flood(x + 1, y)
    flood(x - 1, y)
    flood(x, y + 1)
    flood(x, y - 1)


flood(-1, -1)

# for x in range(-1, len(x_indexes) * 2):
#     for y in range(-1, len(y_indexes) * 2):
#         if (x, y) in flooded:
#             print(".", end="")
#         elif (x, y) in trench:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()


def size(x, y):
    if x % 2 == 0:
        size_x = 1
    else:
        size_x = x_indexes[x // 2 + 1] - x_indexes[x // 2] - 1
    if y % 2 == 0:
        size_y = 1
    else:
        size_y = y_indexes[y // 2 + 1] - y_indexes[y // 2] - 1
    return size_x * size_y


print(
    sum(
        size(x, y)
        for x in range(len(x_indexes) * 2 - 1)
        for y in range(len(y_indexes) * 2 - 1)
        if (x, y) not in flooded
    )
)
# 78242031808225
