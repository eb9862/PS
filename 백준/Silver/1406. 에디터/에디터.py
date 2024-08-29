from collections import deque
from sys import stdin
input = stdin.readline

l = list(input().rstrip())
r = deque([])
M = int(input().rstrip())
for _ in range(M):
    lst = list(input().rstrip().split())
    if lst[0] == 'P':
        l.append(lst[1])
    else:
        if lst[0] == 'L' and l != []:
            r.appendleft(l.pop())
        elif lst[0] == 'D' and r != deque([]):
            l.append(r.popleft())
        elif lst[0] == 'B' and l != []:
            l.pop()
for i in r:
    l.append(i)
res = ''.join(l)
print(res)