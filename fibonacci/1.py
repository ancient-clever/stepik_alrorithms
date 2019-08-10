def fib(n):
    f = [0, 1]
    if n > 1:
        for r in range(2, n+1):
            i = f[r-1] + f[r-2]
            f.append(i)
    return f[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
