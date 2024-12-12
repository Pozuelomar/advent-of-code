import sys
from collections import Counter

arr = []
for line in sys.stdin:
    arr.append(list(line.strip("\n")))

regions = [[None for _ in l] for l in arr]


def dfs(x, y, color):
    if x < 0 or x >= len(arr) or y < 0 or y >= len(arr[x]):
        return
    if regions[x][y] is not None:
        return
    if arr[x][y] != arr[color[0]][color[1]]:
        return
    regions[x][y] = color
    dfs(x + 1, y, color)
    dfs(x - 1, y, color)
    dfs(x, y + 1, color)
    dfs(x, y - 1, color)


for i in range(len(arr)):
    for j in range(len(arr[i])):
        dfs(i, j, (i, j))

print(regions)

areas = Counter([r for l in regions for r in l])

print(areas)


def perimeter(x, y):
    s = set()

    def foo(i, j):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]):
            return 1
        if regions[i][j] != (x, y):
            return 1
        if (i, j) in s:
            return 0
        s.add((i, j))
        return sum([foo(i + 1, j), foo(i - 1, j), foo(i, j + 1), foo(i, j - 1)])

    return foo(x, y)


s = 0
for (x, y), v in areas.items():
    p = perimeter(x, y)
    # print((x, y), v, p)
    s += v * p

print(s)
