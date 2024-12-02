import sys

garden = sys.stdin.read().splitlines()

for i, l in enumerate(garden):
    for j, c in enumerate(l):
        if c == "S":
            start = (i, j)


def neighbours(x, y):
    for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= i < len(garden) and 0 <= j < len(garden[0]):
            if garden[i][j] != "#":
                yield (i, j)


# def neighbours(x, y):
#     for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#         # if 0 <= i < len(garden) and 0 <= j < len(garden[0]):
#         if garden[i % len(garden)][j % len(garden[0])] != "#":
#             yield (i, j)


def solve(start, steps):
    s = {start}
    for _ in range(steps):
        s = set((i, j) for x, y in s for i, j in neighbours(x, y))
    return len(s)


STEPS = 26501365
# STEPS is 26501365 = (131 * 202300) + 65

# STEPS = 5000
# STEPS = 16
MAP_SIZE = len(garden)
N = STEPS // MAP_SIZE

print(STEPS, MAP_SIZE, N)

leftover = (STEPS - MAP_SIZE // 2 - 1) % MAP_SIZE
tips = 0
for start in [
    (MAP_SIZE - 1, MAP_SIZE // 2),
    (0, MAP_SIZE // 2),
    (MAP_SIZE // 2, MAP_SIZE - 1),
    (MAP_SIZE // 2, 0),
]:
    tips += solve(start, leftover)
print(tips)
# tips = 22740

leftover = (STEPS - MAP_SIZE - 1) % MAP_SIZE
small_corner = 0
for start in [
    (0, 0),
    (0, MAP_SIZE - 1),
    (MAP_SIZE - 1, 0),
    (MAP_SIZE - 1, MAP_SIZE - 1),
]:
    small_corner += solve(start, leftover)
print(small_corner)
# small_corner = 3841

leftover = (STEPS - MAP_SIZE - 1) % MAP_SIZE + MAP_SIZE
big_corner = 0
for start in [
    (0, 0),
    (0, MAP_SIZE - 1),
    (MAP_SIZE - 1, 0),
    (MAP_SIZE - 1, MAP_SIZE - 1),
]:
    big_corner += solve(start, leftover)
print(big_corner)
# big_corner = 6595

full_center = solve((MAP_SIZE // 2, MAP_SIZE // 2), 501)
print(full_center)
full_shifted = solve((MAP_SIZE // 2, MAP_SIZE // 2), 500)
print(full_shifted)


total = (
    tips
    + small_corner * (N)
    + big_corner * (N - 1)
    + full_center * ((N) ** 2)
    + full_shifted * ((N - 1) ** 2)
)
print(
    tips,
    "+",
    small_corner,
    "*",
    N,
    "+",
    big_corner,
    "*",
    N - 1,
    "+",
    full_center,
    "*",
    (N + 1) ** 2,
    "+",
    full_shifted,
    "*",
    N * N,
)
print(total)
# 615771078140747 too low
# 618431221990747 too high
# 618267520830747 nope


# print(16733044)  # 5000
