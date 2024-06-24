import heapq as hq
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())
hp = []
l = 0
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if l == 0:
            print(str(0) + '\n')
        else:
            print(str(hq.heappop(hp) * (-1)) + '\n')
            l -= 1
    else:
        hq.heappush(hp, -x)
        l += 1