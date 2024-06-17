from sys import stdin
input = stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    lst = []
    for _ in range(n):
        lst.append(input().rstrip().split()[1])
    s = set(lst)
    cal_lst = []
    for k in s:
        cal_lst.append(lst.count(k))
    sum = 1
    for i in cal_lst:
        sum = sum * (i + 1)
    sum -= 1
    print(sum)