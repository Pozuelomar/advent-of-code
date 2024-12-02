import sys
from collections import Counter

arr = []
for line in sys.stdin:
    x, y = map(int, line.split())
    arr.append([x, y])

# print(arr)

arr = [sorted(x) for x in zip(*arr)]

print(arr)

a = arr[0]
b = arr[1]
c = Counter(b)
s = 0
for x in a:
    if x in c:
        s += x * c[x]
print(s)
