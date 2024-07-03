N = int(input())

def cnt_l(n):
    cnt = 1
    while True:
        n = n // 10
        if n == 0:
            break
        cnt += 1
    return cnt

l = cnt_l(N)

res = 0
if l == 1:
    print(N)
else:
    res += (N - 10**(l-1) + 1) * l
    l -= 1
    while l != 1:
        res += (10**l - 10**(l-1)) * l
        l -= 1
    res += 9
    print(res)