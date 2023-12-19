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
        return prod(v[1] - v[0] + 1 for v in value.values())
    if label == "R":
        return 0

    def process_condition(cd):
        if ":" not in cd:
            return count_accepted(value, cd)
        var, op, val, dest = re.match(r"(\w+)([<>])(\d+):(\w+)", cd).groups()
        match op:
            case ">" if value[var][0] > int(val):
                return count_accepted(value, dest)
            case ">" if value[var][1] <= int(val):
                return 0
            case ">":
                old_v = value[var][0]
                value[var][0] = int(val) + 1
                x = count_accepted(value, dest)
                value[var][0] = old_v
                value[var][1] = int(val)
                return x
            case "<" if value[var][1] < int(val):
                return count_accepted(value, dest)
            case "<" if value[var][0] >= int(val):
                return 0
            case "<":
                old_v = value[var][1]
                value[var][1] = int(val) - 1
                x = count_accepted(value, dest)
                value[var][1] = old_v
                value[var][0] = int(val)
                return x

    return sum(process_condition(cd) for cd in instructions[label])


print(
    count_accepted(
        {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]},
        "in",
    )
)
# 126107942006821
