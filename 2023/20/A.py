import sys
from collections import defaultdict, deque

all_nodes = {}
for line in sys.stdin.read().splitlines():
    key, nodes = line.split(" -> ")
    if key == "broadcaster":
        broadcaster = nodes.split(", ")
    else:
        all_nodes[key[1:]] = (key[0], nodes.split(", "))

flip_flops = {}
for node, (type, nodes) in all_nodes.items():
    if type == "%":
        flip_flops[node] = False

conjunctions = defaultdict(dict)
for node, (type, nodes) in all_nodes.items():
    for n in nodes:
        if n in all_nodes:
            if all_nodes[n][0] == "&":
                conjunctions[n][node] = False

totals = [0, 0]


def send_pulse():
    pulses = deque([("broadcaster", False, "button")])
    while pulses:
        key, strength, from_ = pulses.popleft()
        # print(from_, ["-low->", "-high->"][strength], key)
        totals[strength] += 1
        if key in flip_flops:
            if strength:
                continue
            flip_flops[key] = not flip_flops[key]
            for n in all_nodes[key][1]:
                pulses.append((n, flip_flops[key], key))
            continue
        if key in conjunctions:
            conjunctions[key][from_] = strength
            for n in all_nodes[key][1]:
                pulses.append((n, not all(conjunctions[key].values()), key))
            continue
        if key == "broadcaster":
            for n in broadcaster:
                pulses.append((n, strength, key))
            continue


for i in range(1000):
    send_pulse()

print(totals[0] * totals[1])
