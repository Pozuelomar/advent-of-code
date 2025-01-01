import sys
from collections import defaultdict


connections = defaultdict(set)
for line in sys.stdin:
    a, b = line.strip().split("-")
    connections[a].add(b)
    connections[b].add(a)


connected = []

for a in connections:
    for b in connections:
        for c in connections:
            if b in connections[a] and c in connections[b] and a in connections[c]:
                connected.append((a, b, c))

s = 0
for a, b, c in connected:
    if a.startswith("t") or b.startswith("t") or c.startswith("t"):
        s += 1

print(s // 6)  # removing permutations
