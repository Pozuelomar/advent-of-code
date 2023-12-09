import sys
from collections import defaultdict

conversions = defaultdict(list)
converts_to = {}


def convert(type_, value):
    assert type_ in conversions
    for a, b, length in conversions[type_]:
        if value >= a and value < a + length:
            return converts_to[type_], b + value - a
    return converts_to[type_], value


for line in sys.stdin:
    if ":" in line:
        if line.startswith("seeds:"):
            seeds = [int(v) for v in line.split(":")[1].split()]
            continue
        line = line.split()[0].split("-")
        conversion = line[0]
        converts_to[line[0]] = line[2]
        continue
    if not line.strip():
        continue
    dest, source, length = [int(v) for v in line.split()]
    conversions[conversion].append((source, dest, length))


def min_location(type_, value):
    if type_ == "location":
        return value
    return min_location(*convert(type_, value))


# print(conversions)
# print(converts_to)
min_ = 10**100
for seed in seeds:
    value = min_location("seed", seed)
    min_ = min(min_, value)
print(min_)
# 170017547 too low
