import sys
from collections import Counter

order = "J23456789TQKA"

hands = []
for line in sys.stdin:
    hand, bid = line.strip().split()
    count = Counter(hand)
    js = count.pop("J", 0)
    combo = sorted(count.values(), reverse=True) or [0]
    combo[0] += js
    hands.append((combo, [order.index(c) for c in hand], int(bid)))

total = sum((i + 1) * bid for (i, (_, _, bid)) in enumerate(sorted(hands)))
print(total)
# 248256639
