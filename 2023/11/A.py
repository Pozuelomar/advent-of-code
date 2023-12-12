import sys
from itertools import chain

image = sys.stdin.read().splitlines()
image = chain(*[(l, l) if all(c == "." for c in l) else (l,) for l in image])
image = zip(*image)
image = chain(*[(l, l) if all(c == "." for c in l) else (l,) for l in image])
image = list(image)

positions = {(i, j) for i, l in enumerate(image) for j, v in enumerate(l) if v == "#"}

total_distance = sum(
    abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    for pos1 in positions
    for pos2 in positions
    if pos1 < pos2
)
print(total_distance)
# 9684228
