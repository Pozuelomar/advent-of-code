# import sys

# digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# sum = 0
# for line in sys.stdin:
#     l = []
#     for i in range(len(line)):
#         if line[i].isnumeric():
#             l.append(line[i])
#             continue
#         for digit in digits:
#             if line[i:].startswith(digit):
#                 l.append(str(digits.index(digit)))
        
#     n = int(l[0]+l[-1])
#     sum += n

import sys
import re
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def foo(s):
    return s if s.isnumeric() else str(digits.index(s)) 

def search(regex, line):
    v = regex.search(line)
    return line[v.start():v.end()]

sum = 0
digitRegex = re.compile("\d|"+"|".join(digits))
tigidRegex = re.compile("\d|"+"|".join([d[::-1] for d in digits]))
for line in sys.stdin:
    v = search(digitRegex,line)
    w = search(tigidRegex,line[::-1])[::-1]
    sum += int(foo(v)+foo(w))
print(sum)