N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0
for i in lst:
    t += (i // T) + 1
    if (i % T == 0):
        t -= 1

p = N // P
r = N % P
print(t)
print(p, r)