def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)


cache = {}


def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f[n]
        return cache[n]
    return inner


new_fib1 = memo(fib1)


from functools import lru_cache


fib3 = lru_cache(maxsize=None)(fib1)