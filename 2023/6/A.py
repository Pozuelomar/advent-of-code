import sys

times = [int(v) for v in sys.stdin.readline().split()[1:]]
distances = [int(v) for v in sys.stdin.readline().split()[1:]]

product = 1
for time, distance in zip(times, distances):
    total = 0
    for time_pressed in range(0, time+1):
        if time_pressed*(time-time_pressed) > distance:
            total+=1
    product *= total

print(product)