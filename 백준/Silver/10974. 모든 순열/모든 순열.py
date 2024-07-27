n = int(input())

res = []
def bt(lst, l):
    global n, res
    if l == n:
        res.append(lst)
        return
    for i in range(1, n+1):
        if i not in lst:
            bt(lst + [i], l + 1)

bt([], 0)
for case in res:
    print(*case)