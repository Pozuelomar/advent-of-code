import sys
from collections import defaultdict


connections = defaultdict(set)
for line in sys.stdin:
    a, b = line.strip().split("-")
    connections[a].add(b)
    connections[b].add(a)


def foo(nodes, remaining):
    if not remaining:
        return nodes
    max_ = []
    for i, node in enumerate(remaining):
        rem = [n for n in remaining[i + 1 :] if n in connections[node]]
        x = foo(nodes + [node], rem)
        max_ = max(max_, x, key=len)
    return max_


s = foo([], list(connections.keys()))
print(s)

print(",".join(sorted(s)))
