n, m = map(int, input().split())

def fac(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

ans = fac(n) // (fac(n-m) * fac(m))
print(ans)