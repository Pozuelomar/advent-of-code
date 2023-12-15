import sys

arr = sys.stdin.read().splitlines()
arr = list(zip(*arr))
# print(*arr, sep="\n")

total = 0
for l in arr:
    k = 0
    nb = 0
    for i, v in enumerate(l):
        if v == "#":
            for x in range(k, k + nb):
                total += len(l) - x
            k = i + 1
            nb = 0
        if v == "O":
            nb += 1
    for x in range(k, k + nb):
        total += len(l) - x
print(total)
# 110128
