n, m = map(int, input().split())
left, right = [], []

for i in range(n):
    l, r = map(int, input().split())
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

for i in input().split():
    point = int(i)

    beg, end = 0, n - 1
    while end >= beg:
        j = (beg + end) // 2
        if left[j] > point:
            if  j == beg or left[j - 1] <= point:
                break
            else:
                if j == end:
                    j += 1
                end = j - 1
        else:
            beg = j + 1
            j = j + 1

    beg, end = 0, n - 1
    while end >= beg:
        k = (beg + end) // 2
        if right[k] < point:
            if k == end:
                k += 1
            beg = k + 1
        else:
            if k != beg and right[k - 1] >= point:
                end = k - 1
            else: break

    print(j - k, end = " ")
