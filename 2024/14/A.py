import sys
import re

reg = "p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

h = 103
w = 101
quadrant = {(True, True): 0, (False, True): 0, (True, False): 0, (False, False): 0}
for line in sys.stdin:
    x, y, dx, dy = map(int, re.match(reg, line).groups())
    print(x, y, dx, dy)

    px = (x + 100 * dx) % w
    py = (y + 100 * dy) % h
    print(px, py)
    if px == w // 2 or py == h // 2:
        continue
    quadrant[(px < w // 2, py < h // 2)] += 1

print(
    quadrant[(True, True)]
    * quadrant[(False, False)]
    * quadrant[(True, False)]
    * quadrant[(False, True)]
)
