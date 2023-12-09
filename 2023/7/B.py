import sys
from collections import Counter

order = "J23456789TQKA"

hands = []
for line in sys.stdin:
    hand, bid = line.strip().split()
    count = Counter(hand)
    if "J" in count:
        other_cards = set(count.keys()) - {"J"}
        if other_cards:
            count[max(other_cards, key=count.get)] += count["J"]
            del count["J"]
    hands.append(
        (
            sorted(count.values(), reverse=True),
            [order.index(c) for c in hand],
            int(bid),
        )
    )

hands.sort()
total = sum((i + 1) * bid for (i, (hand, original, bid)) in enumerate(hands))
print(total)
# 248256639
