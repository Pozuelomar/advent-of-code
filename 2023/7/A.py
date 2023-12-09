import sys
from collections import Counter

order = "23456789TJQKA"

hands = []
for line in sys.stdin:
    hand, bid = line.strip().split()
    hands.append(
        (
            sorted(Counter(hand).values(), reverse=True),
            [order.index(c) for c in hand],
            int(bid),
        )
    )

hands.sort()
total = sum((i + 1) * bid for (i, (hand, original, bid)) in enumerate(hands))
print(total)
# 246424613
