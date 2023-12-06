import sys

time = int(''.join(sys.stdin.readline().split()[1:]))
distance = int(''.join(sys.stdin.readline().split()[1:]))

total = 0
for time_pressed in range(0, time+1):
    if time_pressed*(time-time_pressed) > distance:
        total+=1

print(total)