import sys
from collections import Counter
from collections import defaultdict

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
    sides = defaultdict(list)

    def foo(i, j, d):  # d is the direction we came from, encoded as int
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]):
            return sides[d].append((i, j))
        if regions[i][j] != (x, y):
            return sides[d].append((i, j))
        if (i, j) in s:
            return
        s.add((i, j))
        foo(i + 1, j, 1)
        foo(i - 1, j, 2)
        foo(i, j + 1, 3)
        foo(i, j - 1, 4)

    foo(x, y, None)

    print(sides)

    total_sides = 0
    for d, sides_list in sides.items():
        if d == 1 or d == 2:
            sides_list.sort(key=lambda x: (x[0], x[1]))
            for i in range(len(sides_list)):
                if i == 0:
                    total_sides += 1
                elif (sides_list[i][0], sides_list[i][1]) != (
                    sides_list[i - 1][0],
                    sides_list[i - 1][1] + 1,
                ):
                    total_sides += 1
        else:
            sides_list.sort(key=lambda x: (x[1], x[0]))
            for i in range(len(sides_list)):
                if i == 0:
                    total_sides += 1
                elif (sides_list[i][0], sides_list[i][1]) != (
                    sides_list[i - 1][0] + 1,
                    sides_list[i - 1][1],
                ):
                    total_sides += 1
    print(total_sides)
    return total_sides


s = 0
for (x, y), v in areas.items():
    s += v * perimeter(x, y)

print(s)
