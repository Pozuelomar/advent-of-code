import sys
from collections import deque

N = 71
memory = [["." for _ in range(N)] for _ in range(N)]

for _, line in zip(range(1024), sys.stdin):
    x, y = map(int, line.split(","))
    memory[x][y] = "#"

print("\n".join("".join(row) for row in memory))

arr = [[None for _ in range(N)] for _ in range(N)]

# bfs
queue = deque(iterable=[(0, 0, 0)])
while queue:
    x, y, d = queue.popleft()
    if not (0 <= x < N and 0 <= y < N):
        continue
    if arr[x][y] is not None:
        continue
    if memory[x][y] == "#":
        continue
    arr[x][y] = d
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        queue.append((x + dx, y + dy, d + 1))

print(arr[N - 1][N - 1])
