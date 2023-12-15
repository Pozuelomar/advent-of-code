import sys

l = sys.stdin.readline().strip().split(",")


def hash(s):
    x = 0
    for c in s:
        x = ((x + ord(c)) * 17) % 256
    return x


print(sum(hash(s) for s in l))
# 495972
