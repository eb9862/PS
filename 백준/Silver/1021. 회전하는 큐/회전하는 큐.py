from collections import deque

N, M = map(int, input().split())
dq = deque([i for i in range(1, N+1)])

n = list(map(int, input().split()))
res = 0
l = N
for i in range(M):
    target = n[i]
    d = dq.index(target)
    if d == 0:
        dq.popleft()
    elif d < l / 2:
        dq.rotate(-d)
        res += d
        dq.popleft()
    else:
        dq.rotate(l - d)
        res += abs(d - l)
        dq.popleft()
    l -= 1
print(res)