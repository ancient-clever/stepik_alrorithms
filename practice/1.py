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


fib_cache = lru_cache(maxsize=None)(fib1)


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


import time


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


timed(fib3, 800)


from matplotlib import pyplot as plt


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.leggend()
    plt.grid(True)


compare([fib1, fib3], list(range(20)))
