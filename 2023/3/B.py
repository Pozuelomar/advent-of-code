import sys
from collections import defaultdict

l = [line.strip() for line in sys.stdin]


def get(i, j):
    if i < 0 or i >= len(l) or j < 0 or j >= len(l[i]):
        return "."
    return l[i][j]


gears = defaultdict(list)


def store_gear(i, j1, j2, v):
    for a in range(i - 1, i + 2):
        for b in range(j1 - 1, j2 + 2):
            if get(a, b) == "*":
                gears[(a, b)].append(v)


v = 0
length = 0
for i in range(len(l)):
    for j in range(len(l[i]) + 1):
        if get(i, j).isnumeric():
            length += 1
            v = v * 10 + int(get(i, j))
            continue
        if length > 0:
            store_gear(i, j - length, j - 1, v)
            v = 0
            length = 0
            continue
sum = 0
for gear, values in gears.items():
    if len(values) == 2:
        print(gear, values)
        sum += values[0] * values[1]
print(sum)
# 80253814
