from functools import lru_cache

line = [int(i) for i in input().split()]


@lru_cache(None)
def foo(x, steps):
    if steps == 0:
        return 1
    if x == 0:
        return foo(1, steps - 1)
    if len(s := str(x)) % 2 == 0:
        return foo(int(s[len(str(x)) // 2 :]), steps - 1) + foo(
            int(s[: len(str(x)) // 2]), steps - 1
        )
    return foo(x * 2024, steps - 1)


print(sum(foo(x, 75) for x in line))
