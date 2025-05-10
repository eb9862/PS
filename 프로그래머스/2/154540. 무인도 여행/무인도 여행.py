from collections import deque
from typing import List

def is_valid_coor(y: int, x: int, maps: List[str]) -> bool:
    r = len(maps)
    c = len(maps[0])
    
    if (0 <= y and y < r) and (0 <= x and x < c):
        return True
    return False

def bfs(i: int, j: int, visited: List[List[bool]], maps: List[str]) -> int:
    result = 0
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        result += int(maps[y][x])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid_coor(ny, nx, maps) and not visited[ny][nx]:
                if maps[ny][nx] != 'X':
                    q.append((ny, nx))
                    visited[ny][nx] = True
    return result

def solution(maps):
    answer = []
    
    r = len(maps)
    c = len(maps[0])
    visited = [ [ False for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                period = bfs(i, j, visited, maps)
                print(i, j, period)
                answer.append(period)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer