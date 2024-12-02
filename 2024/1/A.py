import sys

arr = []
for line in sys.stdin:
    x, y = map(int, line.split())
    arr.append([x, y])

# print(arr)

arr = [sorted(x) for x in zip(*arr)]

print(arr)

s = 0
for x, y in zip(*arr):
    print(x, y)
    s += abs(x - y)
print(s)
