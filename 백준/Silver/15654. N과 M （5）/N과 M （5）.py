N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

res = []
def bt(list, l):
    global M, lst
    if l == M:
        res.append(list)
        return
    for i in lst:
        if i not in list:
            bt(list + [i], l+1)

bt([], 0)
for i in res:
    print(*i)