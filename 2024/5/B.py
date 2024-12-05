import sys

orders = []
updates = []
section = 1
for line in sys.stdin:
    if section == 1:
        if line == "\n":
            section = 2
        else:
            a, b = map(int, line.split("|"))
            orders.append((a, b))
    else:
        l = [int(x) for x in line.split(",")]
        updates.append(l)


# print(orders)
# print(updates)


s = 0
for u in updates:
    corrected = -1
    for i in range(1000):
        for a, b in orders:
            if a not in u or b not in u:
                continue
            if u.index(a) > u.index(b):
                u[u.index(a)], u[u.index(b)] = u[u.index(b)], u[u.index(a)]
                corrected = i
        if corrected != i:
            break
    if corrected != -1:
        s += u[len(u) // 2]
print(s)
