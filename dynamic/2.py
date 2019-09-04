def bisect(A, x):
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2
        if x > A[m]:
            r = m
        else:
            l = m + 1
    return l

n = int(input())
A = [int(i) for i in input().split()]
D = [10 ** 9 + 1] + [-1 for i in range(n)]
pos = [-1] + [0 for i in range(n)]
prev = [0 for i in range(n)]

length = 0
for i in range(n):
    j = bisect(D, A[i])
    if D[j - 1] >= A[i] and A[i] > D[j]:
        D[j] = A[i]
        pos[j] = i
        prev[i] = pos[j - 1]
        length = max(length, j)

path = []
i = pos[length]
while i != -1:
    path.append(i + 1)
    i = prev[i]

print(length)
for i in reversed(path):
    print(i, end=" ")
print()
