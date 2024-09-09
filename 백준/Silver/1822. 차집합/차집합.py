na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

def binary_search(num):
    global b, cnt, res
    l = 0
    r = nb - 1
    while l <= r:
        m = (l + r) // 2
        if b[m] < num:
            l = m + 1
        elif b[m] > num:
            r = m - 1
        else:
            return 0
    cnt += 1
    return 1

res = []
cnt = 0
for n in a:
    if binary_search(n) == 1:
        res.append(n)
print(cnt)
if cnt != 0:
    print(*res)