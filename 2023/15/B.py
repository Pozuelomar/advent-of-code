import sys

l = sys.stdin.readline().strip().split(",")


def hash(s):
    x = 0
    for c in s:
        x = ((x + ord(c)) * 17) % 256
    return x


boxes = [[] for _ in range(256)]

for op in l:
    if "-" in op:
        key = op[:-1]
        box = hash(key)
        boxes[box] = [(label, focal) for (label, focal) in boxes[box] if label != key]
    elif "=" in op:
        key, focal = op.split("=")
        focal = int(focal)
        box = hash(key)
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == key:
                boxes[box][i] = (key, focal)
                break
        else:
            boxes[box].append((key, focal))


print(boxes)
print(
    sum(
        (i + 1) * (j + 1) * (focal)
        for i, box in enumerate(boxes)
        for j, (label, focal) in enumerate(box)
    )
)
# 245223
