import math
from sys import stdin, stdout
input = stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().rstrip().split())
    # M C N
    res =  math.factorial(M) / (math.factorial(N) * math.factorial(M-N))
    print(int(res))