import sys
import re

regA = "Button A: X\+(\d+), Y\+(\d+)"
regB = "Button B: X\+(\d+), Y\+(\d+)"
regP = "Prize: X=(\d+), Y=(\d+)"

cases = []
for i, line in enumerate(sys.stdin):
    line = line.strip("\n")
    if i % 4 == 0:
        cases.append([])
        x, y = map(int, re.findall(regA, line)[0])
        cases[-1].append((x, y))
    elif i % 4 == 1:
        x, y = map(int, re.findall(regB, line)[0])
        cases[-1].append((x, y))
    elif i % 4 == 2:
        x, y = map(int, re.findall(regP, line)[0])
        cases[-1].append((x + 10000000000000, y + 10000000000000))
    else:
        pass

print(cases)

s = 0
for case in cases:
    a = case[0]
    b = case[1]
    p = case[2]

    # # from the given input, the buttons are never coaxial.
    # if a[0] * b[1] == a[1] * b[0]:
    #     # coaxial
    #     print("coaxial")
    #     continue

    if (p[0] * a[1] - p[1] * a[0]) % (b[0] * a[1] - b[1] * a[0]) != 0:
        continue
    y = (p[0] * a[1] - p[1] * a[0]) // (b[0] * a[1] - b[1] * a[0])

    if (p[0] - b[0] * y) % a[0] != 0:
        continue
    x = (p[0] - b[0] * y) // a[0]

    print(x, y)

    if x < 0 or y < 0:
        continue

    s += x * 3 + y * 1

print(s)
