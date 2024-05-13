from sys import stdin
input = stdin.readline

N = int(input().rstrip())
lst1 = list(map(int, input().rstrip().split()))
lst1.sort()
M = int(input().rstrip())
lst2 = list(map(int, input().rstrip().split()))

for n in lst2:
    l = 0
    r = N-1
    while True:
        m = (l + r) // 2
        if r < l:
            print("0 ", end="")
            break
        if n > lst1[m]:
            l = m + 1
        elif n < lst1[m]:
            r = m - 1
        elif n == lst1[m]:
            print("1 ", end="")
            break