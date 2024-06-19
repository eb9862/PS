import heapq
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

hp = []
lst = []
l = 0

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if l == 0:
            print(str(0) + '\n')
        else:
            res = heapq.heappop(hp)
            if res * (-1) in lst:
                lst.remove(res * (-1))
                print(str(res * (-1)) + '\n')
            else:
                print(str(res) + '\n')
            l -= 1
    else:
        if x < 0:
            heapq.heappush(hp, -x)
            lst.append(x)
        else:
            heapq.heappush(hp, x)
        l += 1