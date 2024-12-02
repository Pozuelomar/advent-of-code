import sys

s = 0
for line in sys.stdin:
    line = [int(x) for x in line.split()]
    diffs = [y - x for x, y in zip(line[:], line[1:])]
    print(line)
    print(diffs)
    if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
        s += 1
print(s)
