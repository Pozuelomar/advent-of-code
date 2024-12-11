line = [int(i) for i in input().split()]

for _ in range(25):
    newline = []
    for v in line:
        if v == 0:
            newline.append(1)
            continue
        if len(s := str(v)) % 2 == 0:
            newline.extend([int(s[len(str(v)) // 2 :]), int(s[: len(str(v)) // 2])])
        else:
            newline.append(v * 2024)
    line = newline


print(len(line))
