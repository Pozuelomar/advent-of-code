import sys
import heapq

array = [[int(c) for c in l] for l in sys.stdin.read().splitlines()]

explored = set()
heap = [(0, (0, 0), (0, 1), -1)]
while heap:
    x, p, d, n = heapq.heappop(heap)
    # print(x, p, d, n)
    if (p, d, n) in explored:
        continue
    explored.add((p, d, n))

    if n >= 10:
        continue
    if not (0 <= p[0] < len(array) and 0 <= p[1] < len(array[0])):
        continue

    if p == (len(array) - 1, len(array[0]) - 1) and n >= 3:
        print(x + array[p[0]][p[1]] - array[0][0])
        break

    heapq.heappush(heap, (x + array[p[0]][p[1]], (p[0] + d[0], p[1] + d[1]), d, n + 1))
    if n >= 3:
        heapq.heappush(
            heap, (x + array[p[0]][p[1]], (p[0] + d[1], p[1] - d[0]), (d[1], -d[0]), 0)
        )
        heapq.heappush(
            heap, (x + array[p[0]][p[1]], (p[0] - d[1], p[1] + d[0]), (-d[1], d[0]), 0)
        )
# 734
