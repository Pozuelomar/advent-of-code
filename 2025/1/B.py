import sys

# digit = 50
# count = 0
# for line in sys.stdin:
#     d=1 if line[0] == 'R' else -1
#     n=int(line[1:])
#     new_digit = (digit +d*n)
#     if new_digit>=100:
#         count+=new_digit//100
#         digit = new_digit %100
#     elif new_digit<0:
#         count+=-(new_digit//100)
#         if digit == 0:
#             count-=1
#         digit = new_digit %100
#         if digit == 0:
#             count+=1
#     elif new_digit == 0:
#         count+=1
#         digit = new_digit


digit = 50
count = 0
for line in sys.stdin:
    d=1 if line[0] == 'R' else -1
    n=int(line[1:])
    for _ in range(n):
        digit = (digit +d) %100
        if digit == 0:
            count+=1

print(count)