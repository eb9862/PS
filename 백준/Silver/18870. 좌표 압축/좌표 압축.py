from sys import stdin
input = stdin.readline

N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
lst2 = list(set(lst))
lst2.sort()

n = len(lst2)

for i in range(N):
    l = 0
    r = n-1
    while l <= r:
        m = (l + r) // 2
        if lst[i] < lst2[m]:
            r = m - 1
        elif lst[i] > lst2[m]:
            l = m + 1
        else:
            print(m, end=" ")
            break