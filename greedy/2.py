from operator import itemgetter


def fit_price(pack_size, items):
    total = 0
    while items:
        if pack_size <= 0:
            break
        price, size, value = items.pop(0)
        if size <= pack_size:
            total += price
            pack_size -= size
        else:
            total += pack_size*value
            pack_size = 0
    return format(float(total), '.3f')


def main():
    n, pack_size = input().split()
    items = []
    for r in range(int(n)):
        price, size = input().split()
        items.append([int(price), int(size), int(price)/int(size)])
    print(fit_price(int(pack_size), sorted(items, key=itemgetter(2), reverse=True)))


if __name__ == "__main__":
    main()
