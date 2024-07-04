from collections import deque

N = int(input())
dq = deque([i for i in range(1, N+1)])

l = N
res = ""
while l != 0:
    res += str(dq.popleft())
    res += " "
    l -= 1
    dq.rotate(-1)

print(res)