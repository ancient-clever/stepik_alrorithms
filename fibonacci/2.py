def fib_digit(n):
    last, current = 0, 1
    for r in range(1, n):
        last, current = current, (last + current) % 10

    return current


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
