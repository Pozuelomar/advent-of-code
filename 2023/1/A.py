import sys

# read lines one by one from input
sum = 0
for line in sys.stdin:
    line = [c for c in line if c.isnumeric()]
    n = int(line[0] + line[-1])
    sum += n

print(sum)
