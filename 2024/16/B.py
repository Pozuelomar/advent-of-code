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


# dijkstra

heap = [(0, start, (0, 1))]
done = set()
costs = {}

while heap:
    cost, pos, dir = heappop(heap)
    if (pos, dir) in done:
        continue
    done.add((pos, dir))

    if cost > 111480:
        break

    if arr[pos[0]][pos[1]] == "#":
        continue

    costs[(pos, dir)] = cost

    for d in [(dir[1], -dir[0]), (-dir[1], dir[0]), dir]:
        if d == dir:
            heappush(heap, (cost + 1, (pos[0] + d[0], pos[1] + d[1]), d))
        else:
            heappush(heap, (cost + 1000, pos, d))

# print(costs)


optimals = set()


def backtrack(pos, dir, cost):
    if costs.get((pos, dir), None) != cost:
        return
    if (pos, dir) in optimals:
        return
    optimals.add((pos, dir))

    backtrack((pos[0] - dir[0], pos[1] - dir[1]), dir, cost - 1)
    backtrack(pos, (dir[1], -dir[0]), cost - 1000)
    backtrack(pos, (-dir[1], dir[0]), cost - 1000)


backtrack(end, (0, 1), 111480)
backtrack(end, (1, 0), 111480)
backtrack(end, (0, -1), 111480)
backtrack(end, (-1, 0), 111480)


print(len(optimals))
poss = {pos for pos, _ in optimals}
# print(poss)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (i, j) in poss:
            print("O", end="")
        else:
            print(arr[i][j], end="")
    print()

print(len(poss))
