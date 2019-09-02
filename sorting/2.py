n = int(input())
cnt = [0 for i in range(11)]
for i in input().split():
    i = int(i)
    cnt[i] += 1
i = 1
while i < 11:
    if cnt[i] == 0:
        i += 1
    else:
        print(i, end=" ")
        cnt[i] -= 1
