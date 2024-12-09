line = input().strip("/n")

memory = []
for i, c in enumerate(line):
    n = int(c)
    if n == 0:
        continue
    if i % 2 == 0:
        memory.append((i // 2, n))
    else:
        memory.append((-1, n))

print(memory)

j = len(memory)
while j > 0:
    j -= 1
    if memory[j][1] == 0 or memory[j][0] == -1:
        continue

    for i in range(j):
        if memory[i][1] == 0:
            continue  # no space
        if memory[i][0] != -1:
            continue  # busy
        if memory[j][1] > memory[i][1]:
            continue  # not enough space

        memory = (
            memory[:i]
            + [(memory[j][0], memory[j][1])]
            + [(memory[i][0], memory[i][1] - memory[j][1])]
            + memory[i + 1 : j]
            + [(memory[i][0], memory[j][1])]
            + memory[j + 1 :]
        )
        print("swapped", i, j)
        j += 1
        break

print(memory)

checksum = 0
i = 0
for x, n in memory:
    for _ in range(n):
        if x != -1:
            checksum += x * i
        i += 1
print(checksum)
