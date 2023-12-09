import sys

time = int("".join(sys.stdin.readline().split()[1:]))
distance = int("".join(sys.stdin.readline().split()[1:]))

# # Brute force
# total = 0
# for time_pressed in range(0, time+1):
#     if time_pressed*(time-time_pressed) > distance:
#         total+=1

# print(total)
# 40651271
# Correct but complexity in time is O(n^2)


# Optimized

#     time_pressed*(time-time_pressed) > distance
# <=> time_pressed*(time-time_pressed) - distance > 0
# <=> (-1)*time_pressed^2 + (time)*time_pressed - distance > 0
# ax^2 + bx + c > 0

a = -1
b = time
c = -distance

delta = b**2 - 4 * a * c
assert delta >= 0, "no roots"

sqrt_delta = delta**0.5

root_1 = (-b - sqrt_delta) / (2 * a)
root_2 = (-b + sqrt_delta) / (2 * a)
root_1, root_2 = sorted([root_1, root_2])

root_1 = int(root_1) + 1  # round up (-ish)
root_2 = int(root_2)  # round dowm

print(root_1, root_2)
print(root_2 - root_1 + 1)
# 40651271
# "Constant" time complexity O(1)
