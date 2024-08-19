N, M = map(int, input().split())
six = [0 for _ in range(M)]
one = [0 for _ in range(M)]
for i in range(M):
    s, o = map(int, input().split())
    six[i] = s
    one[i] = o

six.sort()
one.sort()
min_1 = one[0]
min_6 = six[0]

div = N // 6
rem = N % 6

res = 0
m = min(min_1 * 6, min_6)
res += (div*m)
m = min(min_1*rem, min_6)
res += m
print(res)