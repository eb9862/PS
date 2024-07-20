N, M = map(int, input().split())

res = []
def bt(lst, l):
    if l == M:
        res.append(lst)
        return
    for i in range(1, N+1):
        if l == 0:
            bt(lst + [i], l+1)
        else:
            if lst[-1] <= i:
                bt(lst + [i], l+1)

bt([], 0)
for i in res:
    print(*i)