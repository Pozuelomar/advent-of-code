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


def best_paths_numpad(start, end):
    if start == end:
        yield []
        return
    if start == (3, 0):  # no key here
        return
    if start[0] > end[0]:
        for path in best_paths_numpad((start[0] - 1, start[1]), end):
            yield ["^"] + path
    if start[0] < end[0]:
        for path in best_paths_numpad((start[0] + 1, start[1]), end):
            yield ["v"] + path
    if start[1] > end[1]:
        for path in best_paths_numpad((start[0], start[1] - 1), end):
            yield ["<"] + path
    if start[1] < end[1]:
        for path in best_paths_numpad((start[0], start[1] + 1), end):
            yield [">"] + path


def get_numpad_seqs_(seq):
    if len(seq) == 1:
        yield []
        return
    for path0 in best_paths_numpad(seq[0], seq[1]):
        for path1 in get_numpad_seqs_(seq[1:]):
            yield path0 + ["A"] + path1


def get_numpad_seqs(code):
    seq = [(3, 2)] + [inv_numpad_map[c] for c in code]
    yield from get_numpad_seqs_(seq)


keypad_map = [" ^A", "<v>"]
inv_keypad_map = {
    c: (x, y) for x, row in enumerate(keypad_map) for y, c in enumerate(row)
}


def best_paths_keypad(start, end):
    if start == end:
        yield ""
        return
    if start == (0, 0):  # no key here
        return
    if start[0] > end[0]:
        for path in best_paths_keypad((start[0] - 1, start[1]), end):
            yield "^" + path
    if start[0] < end[0]:
        for path in best_paths_keypad((start[0] + 1, start[1]), end):
            yield "v" + path
    if start[1] > end[1]:
        for path in best_paths_keypad((start[0], start[1] - 1), end):
            yield "<" + path
    if start[1] < end[1]:
        for path in best_paths_keypad((start[0], start[1] + 1), end):
            yield ">" + path


@lru_cache(None)
def best(seq, n):
    # print("  " * (2 - n), seq)
    if n == 0:
        return len(seq)
    s = 0
    for start, end in zip("A" + seq, seq):
        min_ = float("inf")
        for seq2 in best_paths_keypad(inv_keypad_map[start], inv_keypad_map[end]):
            min_ = min(min_, best(seq2 + "A", n - 1))
        s += min_
    return s


def numerical(code):
    x = 0
    for c in code:
        if c.isnumeric():
            x = x * 10 + int(c)
    return x


s = 0
for code in codes:
    a = min(best("".join(seq), 25) for seq in get_numpad_seqs(code))
    print(a)
    b = numerical(code)
    print(b)
    s += a * b

print(s)
