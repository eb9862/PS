N = int(input())
M = int(input())
s = input()

target = 'O'.join((N+1) * 'I')
l = N*2 + 1
cnt = 0
for i in range(M-l+1):
    if s[i] == 'I' and s[i:i+l] == target:
        cnt += 1
print(cnt)