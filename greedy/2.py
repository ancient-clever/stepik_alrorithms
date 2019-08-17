from operator import itemgetter


def fit_price(pack_size, items):
    pass


def main():
    n, pack_size = input().split()
    items = []
    for r in range(int(n)):
        price, size = input().split()
        items.append([int(price), int(size), int(price)/int(size)])
    print(fit_price(pack_size, sorted(items, key=itemgetter(2), reverse=True)))


if __name__ == "__main__":
    main()
