import sys
from collections import defaultdict

arr = []
for line in sys.stdin:
    arr.append(line.strip("\n"))

antenas = defaultdict(list)

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] != ".":
            antenas[arr[i][j]].append((i, j))

print(antenas)

antinodes = set()

for antena in antenas:
    for i in range(len(antenas[antena])):
        for j in range(i + 1, len(antenas[antena])):
            a1 = (
                antenas[antena][i][0] * 2 - antenas[antena][j][0],
                antenas[antena][i][1] * 2 - antenas[antena][j][1],
            )
            a2 = (
                antenas[antena][j][0] * 2 - antenas[antena][i][0],
                antenas[antena][j][1] * 2 - antenas[antena][i][1],
            )
            antinodes.add(a1)
            antinodes.add(a2)

antinodes_inbound = sum(
    [1 for x, y in antinodes if 0 <= x < len(arr) and 0 <= y < len(arr)]
)

print(antinodes_inbound)
