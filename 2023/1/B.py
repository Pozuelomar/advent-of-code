import sys

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum = 0
for line in sys.stdin:
    l = []
    for i in range(len(line)):
        if line[i].isnumeric():
            l.append(line[i])
            continue
        for digit in digits:
            if line[i:].startswith(digit):
                l.append(str(digits.index(digit)))
        
    n = int(l[0]+l[-1])
    sum += n

print(sum)