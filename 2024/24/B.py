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


def print_func(f):
    if f == and_:
        return "AND"
    if f == or_:
        return "OR"
    if f == xor:
        return "XOR"


def print_chart(ops):
    print("```mermaid")
    print("flowchart TD")
    for key, (op, x, y) in sorted(ops.items()):
        print(f"    {x}({x}) -->|{print_func(op)}| {key}({key})")
        print(f"    {y}({y}) -->|{print_func(op)}| {key}({key})")
    print("```")


# print_chart(ops)

# # Find z** that are not a result of a XOR operation
# for z in range(46):
#     if ops[f"z{z:02d}"][0] != xor:
#         print(f"z{z:02d} = {ops[f'z{z:02d}']}")

# z07 = (<built-in function and_>, 'gnj', 'scw')
# z23 = (<built-in function or_>, 'jwb', 'hjp')
# z27 = (<built-in function and_>, 'x27', 'y27')

# # Find their spot manually
# ->
ops["z07"], ops["shj"] = ops["shj"], ops["z07"]
ops["z23"], ops["pfn"] = ops["pfn"], ops["z23"]
ops["z27"], ops["kcd"] = ops["kcd"], ops["z27"]

# print_chart(ops)


def verify():
    z = 0
    for i in range(1000):
        try:
            z += get_value(f"z{i:02d}") << i
        except ValueError:
            break
    x = 0
    for i in range(1000):
        try:
            x += get_value(f"x{i:02d}") << i
        except ValueError:
            break

    y = 0
    for i in range(1000):
        try:
            y += get_value(f"y{i:02d}") << i
        except ValueError:
            break

    return x + y == z


# # Find the remaining swap by brute forcing all swaps that would lead to the right results
# for key1 in ops:
#     for key2 in ops:
#         ops[key1], ops[key2] = ops[key2], ops[key1]
#         try:
#             v = verify()
#             if v:
#                 print(key1, key2)
#         except:
#             pass
#         ops[key1], ops[key2] = ops[key2], ops[key1]


# # Make an alteration in the x** and y** inputs, and keep brute forcing the remaining
# for key1, key2 in [["wkb", "tpk"], ["z16", "wkb"], ["z16", "bfn"], ["z16", "hbd"]]:
#     ops[key1], ops[key2] = ops[key2], ops[key1]
#     try:
#         v = verify()
#         if v:
#             print(key1, key2)
#     except:
#         pass
#     ops[key1], ops[key2] = ops[key2], ops[key1]


ops["wkb"], ops["tpk"] = ops["tpk"], ops["wkb"]


print_chart(ops)
print(verify())


keys = ["z07", "shj", "z23", "pfn", "z27", "kcd", "wkb", "tpk"]
print(",".join(sorted(keys)))
