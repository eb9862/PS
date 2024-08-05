from sys import stdin
input = stdin.readline

N = int(input().rstrip())

lst = [0 for _ in range(N)]
for i in range(N):
    lst[i] = int(input().rstrip())
    
lst.sort(reverse=True)

for i in range(N-2):
    c = lst[i]
    b =lst[i+1]
    a = lst[i+2]
    if c < b + a:
        print(a+b+c)
        exit(0)
print(-1)