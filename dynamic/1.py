n = int(input())
A = [int(i) for i in input().split()]
D = []

for i in range(n):
    D.append(1)
    for j in range(i):
        if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
            D[i] = D[j] + 1

print(max(D) if len(D) else 0)
