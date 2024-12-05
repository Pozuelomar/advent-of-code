import sys

arr = []
for line in sys.stdin:
    arr.append(list(line.strip("\n")))

# print(arr)


def search(x, y):
    if arr[x][y] != "A":
        return 0
    s = ""
    for i, j in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        s += arr[x + i][y + j]
    if s == "MMSS" or s == "SSMM" or s == "MSSM" or s == "SMMS":
        return 1
    return 0


s = 0
for i in range(1, len(arr) - 1):
    for j in range(1, len(arr[i]) - 1):
        s += search(i, j)
print(s)


# 1919 too high
