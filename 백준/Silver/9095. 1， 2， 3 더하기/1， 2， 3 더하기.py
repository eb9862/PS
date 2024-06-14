from sys import stdin
input = stdin.readline

T = int(input())
lst = [0 for _ in range(12)]
lst[1] = 1
lst[2] = 2
lst[3] = 4
for _ in range(T):
    n = int(input())
    if lst[n] != 0:
        print(lst[n])
    else:
        for i in range(4, n + 1):
            lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
        print(lst[n])