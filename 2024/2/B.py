import sys

s = 0
for line in sys.stdin:
    line = [int(x) for x in line.split()]
    for i in range(0, len(line)):
        linei = line[:i] + line[i + 1 :]
        diffs = [y - x for x, y in zip(linei[:], linei[1:])]
        if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
            s += 1
            break

print(s)
