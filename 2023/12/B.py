import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def foo(s, l, opened):
    # print(s, l, opened)
    if s == "":
        if l == (0,) or not l:
            return 1
        return 0
    if opened:
        if not l:
            return 0
        if l[0] == 0:
            if s[0] == "#":
                return 0
            return foo(s[1:], l[1:], False)
        if s[0] == "." and l[0] > 0:
            return 0
        l = list(l)
        l[0] -= 1
        l = tuple(l)
        x = foo(s[1:], l, True)
        return x
    if s[0] == ".":
        return foo(s[1:], l, False)
    if s[0] == "#":
        return foo(s, l, True)
    if s[0] == "?":
        if not l:
            return foo(s[1:], l, False)
        return foo(s, l, True) + foo(s[1:], l, False)


sum_ = 0
for line in sys.stdin:
    s, l = line.strip().split()
    l = [int(c) for c in l.split(",")]
    s = "?".join(s for _ in range(5))
    l *= 5
    x = foo(s, tuple(l), False)
    # print(s, l, x)
    sum_ += x
print(sum_)
# 1909291258644
