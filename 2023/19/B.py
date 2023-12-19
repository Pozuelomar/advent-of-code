import sys
import re
from math import prod

instructions = {}
values = []

for line in sys.stdin.read().splitlines():
    if not line:
        continue
    if line[0] != "{":
        label, value = line.split("{")
        instructions[label] = value[:-1].split(",")
        continue
    values.append(
        {k: int(v) for k, v in (kv.split("=") for kv in line[1:-1].split(","))}
    )


def count_accepted(value, label):
    value = {k: v[:] for k, v in value.items()}
    if label == "A":
        yield prod(v[1] - v[0] + 1 for v in value.values())
        return
    if label == "R":
        yield 0
        return
    for cd in instructions[label]:
        if ":" not in cd:
            yield from count_accepted(value, cd)
            return
        var, op, val, dest = re.match(r"(\w+)([<>])(\d+):(\w+)", cd).groups()
        match op:
            case ">" if value[var][0] > int(val):
                yield from count_accepted(value, dest)
            case ">" if value[var][1] <= int(val):
                continue
            case ">":
                old_v = value[var][0]
                value[var][0] = int(val) + 1
                yield from count_accepted(value, dest)
                value[var][0] = old_v
                value[var][1] = int(val)
            case "<" if value[var][1] < int(val):
                yield from count_accepted(value, dest)
            case "<" if value[var][0] >= int(val):
                continue
            case "<":
                old_v = value[var][1]
                value[var][1] = int(val) - 1
                yield from count_accepted(value, dest)
                value[var][1] = old_v
                value[var][0] = int(val)


print(
    sum(
        count_accepted(
            {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}, "in"
        )
    )
)
# 126107942006821
