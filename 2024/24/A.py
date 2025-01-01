import sys
from operator import and_, or_, xor

values = {}
ops = {}
for line in sys.stdin:
    line = line.strip()
    if ": " in line:
        key, value = line.split(": ")
        values[key] = value
    if " -> " in line:
        a, key = line.split(" -> ")
        x, op, y = a.split(" ")
        match op:
            case "AND":
                ops[key] = (and_, x, y)
            case "OR":
                ops[key] = (or_, x, y)
            case "XOR":
                ops[key] = (xor, x, y)


def get_value(key):
    if key in values:
        return int(values[key])
    if key in ops:
        op, x, y = ops[key]
        x = get_value(x)
        y = get_value(y)
        return op(x, y)
    raise ValueError(f"Unknown key {key}")


print(values)
print(ops)


s = 0
for i in range(1000):
    try:
        s += get_value(f"z{i:02d}") << i
    except ValueError:
        break

print(s)
