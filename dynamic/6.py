def calculator(num):
    sequences = {(num,)}
    while num > 1:
        tmp = set()
        while len(sequences) > 0:
            seq = sequences.pop()
            n = seq[-1]
            a = n // 3 if n % 3 == 0 else None
            b = n // 2 if n % 2 == 0 else None
            c = n - 1
            r = set(filter(None, (a, b, c)))
            for j in r:
                new_seq = seq + (j,)
                if j == 1:
                    return tuple(reversed(new_seq))
                tmp.add(seq + (j,))
        sequences = tmp
    return sequences.pop()


if __name__ == '__main__':
    res = calculator(int(input()))
    print(len(res) - 1)
    print(*res)