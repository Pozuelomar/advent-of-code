import sys

pads = []
locks = []

last = []
for line in list(sys.stdin) + ["\n"]:
    line = line.strip()
    if not line:
        if last[0] == ".....":
            transposed = list(zip(*last))
            v = [l.count("#") - 1 for l in transposed]
            pads.append(v)
        else:
            transposed = list(zip(*last))
            v = [l.count("#") - 1 for l in transposed]
            locks.append(v)
        last = []
    else:
        last.append(line)


print(pads)
print(locks)
print(len(pads), len(locks))

s = 0
for pad in pads:
    for lock in locks:
        if all(a + b <= 5 for a, b in zip(pad, lock)):
            s += 1

print(s)
