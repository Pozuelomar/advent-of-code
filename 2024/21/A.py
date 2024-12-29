import sys
from collections import defaultdict
from functools import lru_cache


codes = []

for line in sys.stdin:
    codes.append(line.strip())

print(codes)

numpad_map = ["789", "456", "123", " 0A"]
inv_numpad_map = {
    c: (x, y) for x, row in enumerate(numpad_map) for y, c in enumerate(row)
}

print(inv_numpad_map)


@lru_cache(None)
def best_paths_numpad(start, end):
    if start == end:
        return [[]]
    if start == (3, 0):  # no key here
        return []
    l = []
    if start[0] > end[0]:
        for path in best_paths_numpad((start[0] - 1, start[1]), end):
            l.append(["^"] + path)
    if start[0] < end[0]:
        for path in best_paths_numpad((start[0] + 1, start[1]), end):
            l.append(["v"] + path)
    if start[1] > end[1]:
        for path in best_paths_numpad((start[0], start[1] - 1), end):
            l.append(["<"] + path)
    if start[1] < end[1]:
        for path in best_paths_numpad((start[0], start[1] + 1), end):
            l.append([">"] + path)
    return l


# @lru_cache(None)
def get_numpad_seqs_(seq):
    if len(seq) == 1:
        yield []
        return
    # print(seq)
    paths0 = list(best_paths_numpad(seq[0], seq[1]))
    paths1 = list(get_numpad_seqs_(seq[1:]))
    for path0 in paths0:
        for path1 in paths1:
            yield path0 + ["A"] + path1


# @lru_cache(None)
def get_numpad_seqs(code):
    # print(code)
    seq = [(3, 2)] + [inv_numpad_map[c] for c in code]
    # print(seq)
    yield from get_numpad_seqs_(seq)


# for code in codes[:1]:
#     get_keypad_seqs(code)

# for x in get_numpad_seqs("029A"):
#     print("".join(x))


keypad_map = [" ^A", "<v>"]
inv_keypad_map = {
    c: (x, y) for x, row in enumerate(keypad_map) for y, c in enumerate(row)
}


@lru_cache(None)
def best_paths_keypad(start, end):
    if start == end:
        return [[]]
    if start == (0, 0):  # no key here
        return []
    l = []
    if start[0] > end[0]:
        for path in best_paths_keypad((start[0] - 1, start[1]), end):
            l.append(["^"] + path)
    if start[0] < end[0]:
        for path in best_paths_keypad((start[0] + 1, start[1]), end):
            l.append(["v"] + path)
    if start[1] > end[1]:
        for path in best_paths_keypad((start[0], start[1] - 1), end):
            l.append(["<"] + path)
    if start[1] < end[1]:
        for path in best_paths_keypad((start[0], start[1] + 1), end):
            l.append([">"] + path)
    return l


# @lru_cache(None)
def get_keypad_seqs_(seq):
    # print(seq)
    if len(seq) == 1:
        return [[]]
    # print(seq)
    l = []
    paths0 = list(best_paths_keypad(seq[0], seq[1]))
    paths1 = list(get_keypad_seqs_(seq[1:]))

    for path0 in paths0:
        for path1 in paths1:
            l.append(path0 + ["A"] + path1)
    # print(l)
    return l


# @lru_cache(None)
def get_keypad_seqs(code):
    # print(code)
    seq = [(0, 2)] + [inv_keypad_map[c] for c in code]
    # print(seq)
    yield from get_keypad_seqs_(seq)


def filter_non_minimal(l):
    # return l
    len_dict = defaultdict(list)
    for x in l:
        len_dict[len(x)].append(x)

    return len_dict[min(len_dict.keys())]


def min_code(code):
    min_ = float("inf")
    l = filter_non_minimal(get_numpad_seqs(code))
    for _ in range(2):
        newl = []
        for x in l:
            newl.extend(get_keypad_seqs(x))
        l = filter_non_minimal(newl)
    return min([len(x) for x in l])


def numerical(code):
    x = 0
    for c in code:
        if c.isnumeric():
            x = x * 10 + int(c)
    return x


# print(min_code("029A"))
# print(numerical("029A"))

s = 0
for code in codes:
    a = min_code(code)
    print(a)
    b = numerical(code)
    print(b)
    s += a * b

assert s == 203814, s
print(s)
