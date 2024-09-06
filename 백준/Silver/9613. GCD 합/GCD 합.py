import math
from sys import stdin
input = stdin.readline

t = int(input().rstrip())
for _ in range(t):
    lst = list(map(int, input().rstrip().split()))
    n = lst[0]
    res = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            res += math.gcd(lst[i], lst[j])
    print(res)