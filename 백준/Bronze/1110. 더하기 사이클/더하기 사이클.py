N = int(input())

l = N // 10
r = N % 10
new = (r * 10) + ((l + r) % 10)
n = 1
while new != N:
    l = new // 10
    r = new % 10
    new = (r * 10) + ((l + r) % 10)
    n += 1
print(n)