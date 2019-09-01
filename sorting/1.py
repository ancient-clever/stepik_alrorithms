def count_pairs(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


def main():
    n = int(input())
    row = [int(number) for number in input().split()]
    pairs = count_pairs(row, n)
    print(pairs)


if __name__ == "__main__":
    main()
