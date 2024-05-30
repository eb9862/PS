from sys import stdin
from sys import stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())
lst = [0 for i in range(10001)]

for _ in range(N):
    num = int(input().rstrip())
    lst[num] += 1

for i in range(10001):
    if (lst[i] != 0):
        for j in range(lst[i]):
            print(str(i) + '\n')