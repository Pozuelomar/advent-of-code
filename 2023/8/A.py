import sys

directions = sys.stdin.readline().strip()
sys.stdin.readline()
map = {line[:3]: (line[7:10], line[12:15]) for line in sys.stdin}

steps = 0
area = 'AAA'
while area != 'ZZZ':
    area = map[area][directions[steps % len(directions)]=='R']
    steps += 1

print(steps)
#18113