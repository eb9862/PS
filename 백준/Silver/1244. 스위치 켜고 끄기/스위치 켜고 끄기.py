from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
M = int(input().rstrip())

for _ in range(M):
    s, n = map(int, input().rstrip().split())
    if s == 1:
        for i in range(N):
            if (i + 1) % n == 0:
                if lst[i] == 1:
                    lst[i] = 0
                else:
                    lst[i] = 1
    else:
        n -= 1
        for i in range(N):
            if n - i < 0 or n - i >= N or n + i < 0 or n + i >= N:
                break
            else:
                if lst[n-i] != lst[n+i]:
                    break
        if i != 0:
            i -= 1
        for j in range(n-i, n+i+1):
            if lst[j] == 1:
                lst[j] = 0
            else:
                lst[j] = 1

sh = N // 20
re = N % 20

for i in range(sh + 1):
    res = ""
    if i != sh:
        for j in range(20):
            res += str(lst[i * 20 + j])
            if j != 19:
                res += " "
            else:
                print(res + '\n')
    else:
        for j in range(re):
            res += str(lst[i * 20 + j])
            if j != re - 1:
                res += " "
        print(res)