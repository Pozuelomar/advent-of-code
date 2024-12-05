import sys

arr = []
for line in sys.stdin:
    arr.append(list(line.strip("\n")))

# print(arr)


def search(x, y, d):
    s = ""
    for i in range(4):
        if (
            x + d[0] * i < 0
            or x + d[0] * i >= len(arr)
            or y + d[1] * i < 0
            or y + d[1] * i >= len(arr[0])
        ):
            return 0
        s += arr[x + d[0] * i][y + d[1] * i]
    if s == "XMAS":
        return 1
    return 0


directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

s = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for d in directions:
            s += search(i, j, d)
print(s)
