n = int(input())
A = [0] + [int(i) for i in input().split()]

for i in range(2, n + 1):
    A[i] += max(A[i - 1], A[i - 2])
print(A[n])
