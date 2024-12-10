import sys

arr = []
for line in sys.stdin:
    arr.append(list(map(int, line.strip("\n"))))


def get(x, y):
    if x < 0 or x >= len(arr) or y < 0 or y >= len(arr[x]):
        return -1
    return arr[x][y]


dp = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] == 9:
            dp[x][y] = 1
for v in range(8, -1, -1):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == v:
                for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if get(i, j) == v + 1:
                        dp[x][y] += dp[i][j]

s = 0
for larr, ldp in zip(arr, dp):
    for a, d in zip(larr, ldp):
        if a == 0:
            s += d
print(s)
