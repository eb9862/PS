from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())
lst = [0 for i in range(N)]

for i in range(N):
    lst[i] = int(input().rstrip())
lst.sort()
for i in range(N):
    print(str(lst[i]) + '\n')