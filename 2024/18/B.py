import sys
from collections import deque

N = 71
memory = [["." for _ in range(N)] for _ in range(N)]

blockers = []
for line in sys.stdin:
    x, y = map(int, line.split(","))
    blockers.append((x, y))


def init(i):
    memory = [["." for _ in range(N)] for _ in range(N)]
    for x, y in blockers[:i]:
        memory[x][y] = "#"
    return memory


def percolates(memory):
    arr = [[None for _ in range(N)] for _ in range(N)]
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
    return arr[N - 1][N - 1] is not None


for i in range(10000):
    if not percolates(init(i)):
        print(i)
        print(*blockers[i - 1], sep=",")
        break
