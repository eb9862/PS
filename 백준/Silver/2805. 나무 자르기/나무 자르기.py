N, M = map(int, input().split())
lst = list(map(int, input().split()))

mx = max(lst)
r = mx
l = 0

def wood(h):
    global lst
    res = 0
    for i in lst:
        if i > h:
            res += (i - h)
    return res

while l <= r:
    m = (l + r) // 2
    woods = wood(m)
    if woods < M:
        r = m - 1
    else:
        result = m
        l = m + 1
print(result)