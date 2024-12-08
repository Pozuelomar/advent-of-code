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
                antenas[antena][i][0],
                antenas[antena][i][1],
            )
            while 0 <= a1[0] < len(arr) and 0 <= a1[1] < len(arr):
                antinodes.add(a1)
                a1 = (
                    a1[0] + antenas[antena][i][0] - antenas[antena][j][0],
                    a1[1] + antenas[antena][i][1] - antenas[antena][j][1],
                )

            a2 = (
                antenas[antena][j][0],
                antenas[antena][j][1],
            )
            while 0 <= a2[0] < len(arr) and 0 <= a2[1] < len(arr):
                antinodes.add(a2)
                a2 = (
                    a2[0] + antenas[antena][j][0] - antenas[antena][i][0],
                    a2[1] + antenas[antena][j][1] - antenas[antena][i][1],
                )


print(len(antinodes))
