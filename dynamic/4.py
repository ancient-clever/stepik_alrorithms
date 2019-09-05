W, n = map(int, input().split())
w = [int(i) for i in input().split()]
D = [[0 for i in range(n + 1)] for j in range(W + 1)]

for i in range(n):
    for j in range(1, W + 1):
        D[j][i + 1] = D[j][i]
        if w[i] <= j:
            D[j][i + 1] = max(D[j][i + 1], D[j - w[i]][i] + w[i])
print(D[W][n])
