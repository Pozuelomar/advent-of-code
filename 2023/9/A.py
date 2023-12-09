import sys
from functools import lru_cache

sum_ = 0
for line in sys.stdin:
    line = [int(c) for c in line.split()]

    @lru_cache(maxsize=None)
    def foo_down(x, i):
        if i == 0:
            return line[x]
        return foo_down(x + 1, i - 1) - foo_down(x, i - 1)

    def foo_up(x, i):
        if x == 0:
            return 0
        return foo_down(x - 1, i) + foo_up(x - 1, i + 1)

    # print(foo_up(len(line), 0))
    sum_ += foo_up(len(line), 0)
print(sum_)
