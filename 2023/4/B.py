import sys
from collections import defaultdict

cards = defaultdict(int)
for i, line in enumerate(sys.stdin):
    cards[i] += 1
    numbers, winning = line.split(': ')[1].split(' | ')
    for j in range(len(set(numbers.split()) & set(winning.split()))):
        cards[i+1+j] += cards[i]

print(sum(cards.values()))
