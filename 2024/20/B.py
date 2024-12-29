import sys

arr = []

for line in sys.stdin:
    arr.append(line.strip())

distances = [[None for _ in line] for line in arr]

start = None, None
end = None, None

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "S":
            start = i, j
            arr[i] = arr[i][:j] + "." + arr[i][j + 1 :]
        if arr[i][j] == "E":
            end = i, j
            arr[i] = arr[i][:j] + "." + arr[i][j + 1 :]

# dfs
stack = [(start[0], start[1], 0)]
while stack:
    x, y, d = stack.pop()
    if not (0 <= x < len(arr) and 0 <= y < len(arr[x])):
        continue
    if distances[x][y] is not None:
        continue
    if arr[x][y] == "#":
        continue
    distances[x][y] = d
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        stack.append((x + dx, y + dy, d + 1))


print(distances[end[0]][end[1]])

for line in distances:
    print("".join(str(i % 10) if i is not None else "." for i in line))

K = 20
s = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if distances[i][j] is None:
            continue
        for dx in range(-K, K + 1):
            for dy in range(-K, K + 1):
                if abs(dx) + abs(dy) > K:
                    continue
                if not (0 <= i + dx < len(arr) and 0 <= j + dy < len(arr[i + dx])):
                    continue
                if distances[i + dx][j + dy] is None:
                    continue
                if distances[i + dx][j + dy] - distances[i][j] >= 100 + abs(dx) + abs(
                    dy
                ):
                    s += 1

print(s)
