import sys
from collections import defaultdict

cards = defaultdict(int)
for line in sys.stdin:
    card, line = line.split(': ')
    card = int(card.split()[1])
    cards[card] += 1
    numbers, winning = line.split(' | ')
    numbers = set(map(int, numbers.split()))
    winning = set(map(int, winning.split()))
    my_winning = len(numbers & winning)
    for i in range(my_winning):
        cards[card+i+1] += cards[card]

print(sum(cards.values()))
