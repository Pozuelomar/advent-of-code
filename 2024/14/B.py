import sys
import re
import time

reg = "p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

h = 103
w = 101
robots = []
for line in sys.stdin:
    x, y, dx, dy = map(int, re.match(reg, line).groups())
    robots.append([x, y, dx, dy])


for step in range(1, w * h):
    robot_set = set()
    for j, robot in enumerate(robots):
        robot[0] += robot[2]
        robot[0] %= w
        robot[1] += robot[3]
        robot[1] %= h
        robot_set.add((robot[0], robot[1]))

    # horizontal anomaly ferequency
    if step % w != 10:
        continue

    # vertical anomaly frequency
    if step % h != 70:
        continue

    for i in range(h):
        for j in range(w):
            if (i, j) in robot_set:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print(step)

    # # pause 10ms
    # time.sleep(0.1)
