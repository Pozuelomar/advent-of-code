import sys
import re

s = 0
do = True
for line in sys.stdin:
    reg = "mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)"
    print(reg)
    for match in re.finditer(reg, line):
        print(match.group(0))
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif do:
            print(match.group(1), match.group(2))
            s += int(match.group(1)) * int(match.group(2))

print(s)
