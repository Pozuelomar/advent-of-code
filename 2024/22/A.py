import sys


def foo(secret, i):
    for _ in range(i):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
    return secret


s = 0
for line in sys.stdin:
    secret = int(line)
    s += foo(secret, 2000)
print(s)
