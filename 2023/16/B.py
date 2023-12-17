import sys
import numpy as np

mirrors = sys.stdin.read().splitlines()


sys.setrecursionlimit(100000)

beamed = set()


def beam(p, d):
    if not (0 <= p[0] < len(mirrors) and 0 <= p[1] < len(mirrors[0])):
        return
    if (tuple(p), tuple(d)) in beamed:
        return
    beamed.add((tuple(p), tuple(d)))

    if mirrors[p[0]][p[1]] == "-" and d[0] != 0:
        for d in [np.array([0, 1]), np.array([0, -1])]:
            beam(p + d, d)
        return
    if mirrors[p[0]][p[1]] == "|" and d[1] != 0:
        for d in [np.array([1, 0]), np.array([-1, 0])]:
            beam(p + d, d)
        return

    if mirrors[p[0]][p[1]] == "/":
        d = np.array([-d[1], -d[0]])
    if mirrors[p[0]][p[1]] == "\\":
        d = np.array([d[1], d[0]])
    return beam(p + d, d)


def score(p, d):
    global beamed
    beamed = set()
    beam(p, d)

    return len({p for p, d in beamed})


print(
    max(
        [score(np.array([i, 0]), np.array([0, 1])) for i in range(len(mirrors))]
        + [
            score(np.array([len(m) - 1, i]), np.array([-1, 0]))
            for i, m in enumerate(mirrors)
        ]
        + [
            score(np.array([i, len(m) - 1]), np.array([0, -1]))
            for i, m in enumerate(mirrors)
        ]
        + [score(np.array([0, i]), np.array([1, 0])) for i in range(len(mirrors[0]))]
    )
)
# 8231
