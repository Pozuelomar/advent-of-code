import sys
from collections import defaultdict, deque
from math import prod

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


# def print_graph():
#     print("```mermaid")
#     print("flowchart TD")
#     for n in broadcaster:
#         print(f"    broadcaster --> {n}")
#     for key in flip_flops:
#         for n in all_nodes[key][1]:
#             print(f"    {key}({key}) --> {n}")
#     for key in conjunctions:
#         for n in all_nodes[key][1]:
#             print(f"    {key}[{key}] --> {n}")
#     print("```")


# print_graph()

last = defaultdict(int)
diff = defaultdict(int)


def send_pulse():
    pulses = deque([("broadcaster", False, "button")])
    while pulses:
        key, strength, from_ = pulses.popleft()
        # print(from_, ["-low->", "-high->"][strength], key)

        # These are the 4 keys before the final one
        if key in ["fh", "lk", "hh", "fn"] and strength == False:
            # print(key, i + 1 - last[key])
            diff[key] = i + 1 - last[key]
            last[key] = i + 1

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
    return False


for i in range(100_000):
    send_pulse()

print(prod(diff.values()))
# 238815727638557
