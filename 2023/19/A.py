import sys

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


def is_accepted(value, label):
    if label == "A":
        return True
    if label == "R":
        return False
    for instruction in instructions[label]:
        if ":" not in instruction:
            return is_accepted(value, instruction)
        condition, dest = instruction.split(":")
        if eval(condition, dict(value)):
            return is_accepted(value, dest)


print(sum(sum(value.values()) for value in values if is_accepted(value, "in")))
# 575412
