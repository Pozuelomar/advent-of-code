import sys
import numpy as np

arr = sys.stdin.read().splitlines()
# arr = ["#" + l + "#" for l in arr]
# arr.insert(0, "#" * len(arr[0]))
# arr.append("#" * len(arr[0]))
# arr = np.array([list(l) for l in arr])

arr = np.array([list(l) for l in arr])
arr2 = np.full((arr.shape[0] + 2, arr.shape[1] + 2), "#")
arr2[1:-1, 1:-1] = arr
arr = arr2

print(*(map("".join, arr[:5, :5])), sep="\n")
# print(arr)


def move(p, d):
    if arr[*p] == "O":
        if arr[*(p + d)] == ".":
            arr[*(p + d)] = "O"
            arr[*(p)] = "."


def pprint(arr):
    print(*(map("".join, arr)), sep="\n")


# Very slow, but works.
def cycle(arr):
    # north, then west, then south, then east.
    for d in [np.array([-1, 0]), np.array([0, -1])]:
        pprint(arr)
        key = None
        new_key = tuple(map(tuple, arr))
        while key != new_key:
            key = new_key
            for i in range(1, arr.shape[0] - 1):
                for j in range(1, arr.shape[1] - 1):
                    move(np.array([i, j]), d)
            new_key = tuple(map(tuple, arr))

    for d in [np.array([1, 0]), np.array([0, 1])]:
        pprint(arr)
        key = None
        new_key = tuple(map(tuple, arr))
        while key != new_key:
            key = new_key
            for i in range(arr.shape[0] - 2, 0, -1):
                for j in range(arr.shape[1] - 2, 0, -1):
                    move(np.array([i, j]), d)
            new_key = tuple(map(tuple, arr))


seen = {tuple(map(tuple, arr)): 0}
i = 0
while i != 10**9:
    cycle(arr)
    i += 1
    key = tuple(map(tuple, arr))

    if key in seen and (10**9 - i) % (i - seen[key]) == 0:
        print("cycle", seen[key], i)
        break
    seen[key] = i

print(i, seen)
print(*(map("".join, arr)), sep="\n")

total = 0
for i, l in enumerate(arr[::-1]):
    for v in l:
        if v == "O":
            total += i
print(total)
# 103861
