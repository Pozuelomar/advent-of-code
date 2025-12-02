import sys

digit = 50
count = 0
for line in sys.stdin:
    d=1 if line[0] == 'R' else -1
    n=int(line[1:])
    digit = (digit +d*n) %100
    if digit == 0:
        count+=1
        
print(count)