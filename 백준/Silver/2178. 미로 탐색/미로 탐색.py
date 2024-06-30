from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().rstrip().split())
lst = [0 for _ in range(N)]
for i in range(N):
    lst[i] = input().rstrip()

q = deque([(0,0,0)])

while q:
    x, y, cnt = q.popleft()
    if lst[y][x] == '0':
        continue
    if x == M-1 and y == N-1:
        cnt += 1
        print(cnt)
        break
    
    if (x + 1 >= 0 and x + 1 < M) and lst[y][x+1] != '0':
        q.append((x+1, y, cnt+1))
    if (y + 1 >= 0 and y + 1 < N) and lst[y+1][x] != '0':
        q.append((x, y+1, cnt+1))
    if (y - 1 >= 0 and y - 1 < N) and lst[y-1][x] != '0':
        q.append((x, y-1, cnt+1))
    if (x - 1 >= 0 and x - 1 < M) and lst[y][x-1] != '0':
        q.append((x-1, y, cnt+1))
    lst[y] = lst[y][:x] + '0' + lst[y][x+1:]