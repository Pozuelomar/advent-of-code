import sys


def foo(x, a, l):
    if len(l) == 0:
        return x == a
    return foo(x, a + l[0], l[1:]) or foo(x, a * l[0], l[1:])


s = 0
for line in sys.stdin:
    line = line.strip("\n")
    x, l = line.split(": ")
    x = int(x)
    l = list(map(int, l.split()))
    print(x, l)
    if foo(x, l[0], l[1:]):
        s += x

print(s)
