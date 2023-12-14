import sys

arrays = [[]]
for line in sys.stdin:
    line = line.strip()
    if line == "":
        arrays.append([])
        continue
    arrays[-1].append(line)


def check(arr, i):
    return (
        sum(a != b for l1, l2 in zip(arr[i::-1], arr[i + 1 :]) for a, b in zip(l1, l2))
        == 1
    )


sum_ = 0
for array in arrays:
    for i in range(len(array) - 1):
        if check(array, i):
            sum_ += (i + 1) * 100
            break
    else:
        arr = list(zip(*array))
        for i in range(len(arr) - 1):
            if check(arr, i):
                sum_ += (i + 1) * 1
                break
        else:
            print("No match found")
            print(*array, sep="\n")
print(sum_)
# 31603
