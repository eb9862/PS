N = int(input())
M = int(input())
s = input()

cnt = 0
i = 0
last = M-2
n = 0
while i < last:
    if s[i:i+3] == "IOI":
        n += 1
        i += 2
        if n == N:
            cnt += 1
            n -= 1
    else:
        n = 0
        i += 1

print(cnt)