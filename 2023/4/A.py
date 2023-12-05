import sys

sum=0
for line in sys.stdin:
    numbers, winning = line.split(': ')[1].split(' | ')
    numbers = set(map(int, numbers.split()))
    winning = set(map(int, winning.split()))
    my_winning = len(numbers & winning)
    if my_winning:
        sum+=2**(my_winning-1)
print(sum)