def fib(n):
    last, current = 0, 1
    for r in range(1, n):
        last, current = current, last + current

    return current


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
