import sys

image = sys.stdin.read().splitlines()

empty_rows = [all(c == "." for c in l) for l in image]
empty_cols = [all(c == "." for c in l) for l in zip(*image)]

positions = {(i, j) for i, l in enumerate(image) for j, v in enumerate(l) if v == "#"}


def distance(pos1, pos2):
    d = 0
    for empty, *v in zip((empty_rows, empty_cols), pos1, pos2):
        for i in range(*sorted(v)):
            d += 1000000 if empty[i] else 1
    return d


total_distance = sum(
    distance(pos1, pos2) for pos1 in positions for pos2 in positions if pos1 < pos2
)

print(total_distance)
# 483844716556
