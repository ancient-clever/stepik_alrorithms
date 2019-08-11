def gcd(a, b):
    if not a:
        return b
    if not b:
        return a
    if a >= b:
        return gcd(a % b, b)
    if b >= a:
        return gcd(a, b % a)


def main():
    # a, b = map(int, input().split())
    print(gcd(18, 35))


if __name__ == "__main__":
    main()