import sys
from collections import defaultdict

conversions = defaultdict(list)
converts_to = {}

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


def convert(type_, value, remaining_length):
    assert type_ in conversions
    for a, b, length in conversions[type_]:
        if value >= a and value < a + length:
            usable_length = length - (value - a)
            if remaining_length <= usable_length:  # If we use all the length
                yield converts_to[type_], b + value - a, remaining_length
            else:
                yield converts_to[type_], b + value - a, usable_length
                yield from convert(
                    type_, value + usable_length, remaining_length - usable_length
                )  # Continue with the rest of the length
            return
    # Couldn't find a conversion from value
    a, b, length = min(
        [(a, b, length_) for (a, b, length_) in conversions[type_] if a > value]
        + [(10**100, 10**100, 10**100)]
    )
    length_until_next = a - value
    if length_until_next >= remaining_length:  # If no range are accessible
        yield converts_to[type_], value, remaining_length
    else:
        yield converts_to[type_], value, length_until_next
        yield from convert(type_, a, remaining_length - length_until_next)
    return


def min_location(type_, value, length):
    if type_ == "location":
        return value
    return min(min_location(*sub_range) for sub_range in convert(type_, value, length))


# print(conversions)
# print(converts_to)
min_ = min(
    min_location("seed", seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)
)
print(min_)
# 79004094
