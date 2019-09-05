A, B = input(), input()
n, m = len(A), len(B)
D = [list(range(m + 1)) for i in range(2)]

for i in range(n):
    D[(i + 1) & 1][0] = i + 1
    for j in range(m):
        c = (A[i] != B[j])
        insert = D[(i + 1) & 1][j] + 1
        delete = D[i & 1][j + 1] + 1
        replace = D[i & 1][j] + c
        D[(i + 1) & 1][j + 1] = min(insert, delete, replace)

print(D[n & 1][m])
