import sys
from collections import defaultdict

sum = 0
for line in sys.stdin:
    group, line = line.split(": ")
    group = int(group.split()[1])
    colors = defaultdict(int)
    for subgroup in line.split("; "):
        for duet in subgroup.split(", "):
            n, color = duet.split()
            n = int(n)
            color = color
            colors[color] = max(colors[color], n)
    sum += colors["red"] * colors["green"] * colors["blue"]

print(sum)
