from collections import deque
N, K = map(int, input().split())

lst = [i for i in range(2, N+1)]
dq = deque(lst)

rm = 0
brk = 0

while True:
    p = dq.popleft()
    rm += 1
    if rm == K:
        print(p)
        break

    for n in dq.copy():
        if n % p == 0:
            dq.remove(n)
            rm += 1
            if rm == K:
                print(n)
                brk = 1
                break
    if brk == 1:
        break