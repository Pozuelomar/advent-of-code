import sys
from functools import lru_cache

input_arr = []

for line in sys.stdin:
    input_arr.append(line.strip())

towels = [i for i in input_arr[0].split(", ")]

print(towels)


@lru_cache(None)
def possible_patterns(pattern):
    if pattern == "":
        return 1
    return sum(
        possible_patterns(pattern[len(towel) :])
        for towel in towels
        if pattern.startswith(towel)
    )


s = 0
for pattern in input_arr[2:]:
    s += possible_patterns(pattern)

print(s)
