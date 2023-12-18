import sys

directions = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

trench = set(())
pos = (0, 0)
for line in sys.stdin:
    dir, dis, color = line.strip().split()
    dis = int(dis)
    for _ in range(dis):
        trench.add(pos)
        pos = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])

min_x = min(trench, key=lambda x: x[0])[0]
max_x = max(trench, key=lambda x: x[0])[0]
min_y = min(trench, key=lambda x: x[1])[1]
max_y = max(trench, key=lambda x: x[1])[1]

flooded = set()

sys.setrecursionlimit(100000)


def flood(x, y):
    if not (min_x - 1 <= x <= max_x + 1 and min_y - 1 <= y <= max_y + 1):
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


flood(min_x - 1, min_y - 1)
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if (x, y) in flooded:
            print(".", end="")
        elif (x, y) in trench:
            print("#", end="")
        else:
            print(" ", end="")
    print()
print(
    sum(
        1
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
        if (x, y) not in flooded
    )
)
# 39194
