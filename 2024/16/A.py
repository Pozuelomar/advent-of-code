import sys
from functools import lru_cache
from heapq import heappop, heappush

sys.setrecursionlimit(1_000_000_000)


arr = []

for line in sys.stdin:
    arr.append(list(line.strip()))

print(arr)

start = (None, None)
end = (None, None)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "S":
            start = (i, j)
            arr[i][j] = "."
        if arr[i][j] == "E":
            end = (i, j)
            arr[i][j] = "."

print(start, end)


# stack = set()


# @lru_cache(None)
# def foo(pos, dir):
#     print(pos, dir)
#     if pos == end:
#         return 0
#     if arr[pos[0]][pos[1]] == "#":
#         return float("inf")

#     if (pos, dir) in stack:
#         return float("inf")
#     stack.add((pos, dir))
#     m = min(
#         foo((pos[0] + dir[0], pos[1] + dir[1]), dir) + 1,
#         foo(pos, (dir[1], -dir[0])) + 1000,
#         foo(pos, (-dir[1], dir[0])) + 1000,
#     )
#     stack.remove((pos, dir))
#     return m


# print(foo(start, (0, 1)))


# dijkstra

heap = [(0, start, (0, 1))]
done = set()

while heap:
    cost, pos, dir = heappop(heap)
    if (pos, dir) in done:
        continue
    done.add((pos, dir))

    # print(cost)

    if pos == end:
        print(cost)
        break
    if arr[pos[0]][pos[1]] == "#":
        continue

    for d in [(dir[1], -dir[0]), (-dir[1], dir[0]), dir]:
        if d == dir:
            heappush(heap, (cost + 1, (pos[0] + d[0], pos[1] + d[1]), d))
        else:
            heappush(heap, (cost + 1000, (pos[0], pos[1]), d))
