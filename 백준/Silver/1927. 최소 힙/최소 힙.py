import heapq as hq
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())
hp = []
l = 0

for _ in range(N):
    x = int(input().rstrip())
    if x > 0:
        hq.heappush(hp, x)
        l += 1
    else:
        if l == 0:
            print(str(0) + '\n')
        else:
            print(str(hq.heappop(hp)) + '\n')
            l -= 1