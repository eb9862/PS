N, M = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(N):
    res = 0
    for j in range(i, N):
        res += lst[j]
        if res >= M:
            break
    if res == M:
        cnt += 1
print(cnt)