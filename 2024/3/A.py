import sys
import re

s = 0
for line in sys.stdin:
    reg = "mul\\((\\d+),(\\d+)\\)"
    print(reg)
    for match in re.finditer(reg, line):
        print(match.group(1), match.group(2))
        s += int(match.group(1)) * int(match.group(2))

print(s)
