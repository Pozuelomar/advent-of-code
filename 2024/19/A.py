import sys
from functools import lru_cache

input_arr = []

for line in sys.stdin:
    input_arr.append(line.strip())

towels = [i for i in input_arr[0].split(", ")]

print(towels)


@lru_cache(None)
def is_possible(pattern):
    if pattern == "":
        return 1
    for towel in towels:
        if pattern.startswith(towel) and is_possible(pattern[len(towel) :]):
            return 1
    return 0


s = 0
for pattern in input_arr[2:]:
    s += is_possible(pattern)

print(s)
