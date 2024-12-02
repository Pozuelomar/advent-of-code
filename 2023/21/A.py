import sys

garden = sys.stdin.read().splitlines()

for i, l in enumerate(garden):
    for j, c in enumerate(l):
        if c == "S":
            start = (i, j)


def neighbours(x, y):
    for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= i < len(garden) and 0 <= j < len(garden[0]):
            if garden[i][j] != "#":
                yield (i, j)


s = {start}
for _ in range(64):
    s = set((i, j) for x, y in s for i, j in neighbours(x, y))

print(len(s))
# 3743
