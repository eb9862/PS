from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())

for _ in range(N):
    lst = list(map(int, input().rstrip().split()))
    n = lst[0]
    avg = sum(lst[1:n+1]) / n
    over = sum([i > avg for i in lst[1:n+1]])
    print(str(round(over / n * 100, 3)) + '%\n')