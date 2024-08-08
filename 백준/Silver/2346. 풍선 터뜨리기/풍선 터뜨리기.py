from collections import deque
n = int(input())
lst = list(map(int, input().split()))
val = deque(lst)
balloon = deque([i for i in range(1, n+1)])

res = []
l = n
while l != 0:
    mv = val.popleft()
    num = balloon.popleft()
    l -= 1
    res.append(num)
    if mv > 0:
        val.rotate(-(mv-1))
        balloon.rotate(-(mv-1))
    else:
        val.rotate(-mv)
        balloon.rotate(-mv)
print(*res)