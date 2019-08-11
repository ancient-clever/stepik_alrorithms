def fib_mod(n, m):
    period = [0, 1]
    last, current = period
    for r in range(1, n):
        old = current
        current = (last + current) % m
        last = old
        if last == 0 and current == 1:
            period.pop()
            break
        else:
            period.append(current)

    return period[n % len(period)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
