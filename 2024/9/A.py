line = input().strip("/n")

memory = []
for i, c in enumerate(line):
    n = int(c)
    if i % 2 == 0:
        memory.extend([i // 2] * n)
    else:
        memory.extend([-1] * n)

print(memory)

i = 0
j = len(memory) - 1
while i < j:
    if memory[i] != -1:
        i += 1
        continue
    if memory[j] == -1:
        j -= 1
        continue
    memory[i], memory[j] = memory[j], memory[i]
    i += 1
    j -= 1

print(memory)

checksum = 0
for i, n in enumerate(memory):
    if n == -1:
        break
    checksum += i * n

print(checksum)
