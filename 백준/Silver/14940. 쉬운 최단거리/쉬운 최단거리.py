from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

maps = [ [ 0 for _ in range(m) ] for _ in range(n) ]
result = [ [ 0 for _ in range(m) ] for _ in range(n) ]
visited = [ [ False for _ in range(m) ] for _ in range(n) ]

for y in range(n):
    maps[y] = list(map(int, input().strip().split()))
    if 2 in maps[y]:
        target = (y, maps[y].index(2))

def is_valid_coor(y: int, x: int) -> bool:
    global n, m
    
    if y < 0 or y >= n:
        return False
    if x < 0 or x >= m:
        return False
    return True

def bfs(target_y: int, target_x: int):
    global visited, maps, result
    
    q = deque([(target_y, target_x)])
    visited[target_y][target_x] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not is_valid_coor(ny, nx):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if maps[ny][nx] == 0:
                continue
            
            result[ny][nx] = result[y][x] + 1
            q.append((ny, nx))

bfs(target[0], target[1])
for y in range(n):
    for x in range(m):
        if (not visited[y][x]) and maps[y][x] == 1:
            result[y][x] = -1

for y in range(n):
    print(*result[y])