a, b, c = map(int, input().split())

def cal_power(x, n):
    global c
    if n == 1:
        return x % c
    else:
        half = cal_power(x, n // 2)
        if n % 2 == 0:
            return half % c * half % c
        else:
            return half % c * half % c * x

print(cal_power(a, b) % c)