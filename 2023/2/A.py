import sys
from collections import defaultdict

target_colors = {"red": 12, "green": 13, "blue": 14}

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
    if all(
        [colors[color] <= target_colors[color] for color in ["red", "green", "blue"]]
    ):
        sum += group

print(sum)
