import sys
from collections import Counter


def diffs(secret, i):
    for _ in range(i):
        last = secret
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        yield (secret % 10) - (last % 10)


def values(secret, i):
    for _ in range(i):
        last = secret
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        yield secret % 10


def simulate(secret):
    s = Counter()
    l = list(diffs(secret, 2000))
    l_secret = list(values(secret, 2000))
    for i in range(2000 - 3):
        key = tuple(l[i : i + 4])
        if key not in s:
            s[key] = l_secret[i + 3]
    return s


d = Counter()
for line in sys.stdin:
    secret = int(line)
    s = simulate(secret)
    d += s

print(max(d.values()))
