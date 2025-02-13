from collections import deque

def solution(storage, requests):
    
    n = len(storage)
    m = len(storage[0])
    answer = n * m
    
    grid = []
    for i in range(n):
        grid.append(list(storage[i]))

    is_connected = [ [False for _ in range(m)] for _ in range(n) ]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                is_connected[i][j] = True

                
    def is_valid_position(y: int, x: int) -> bool:
        return (x in range(m)) and (y in range(n))
    
    def bfs(y: int, x: int, visited: list):
        
        q = deque([(y, x)])
        visited[y][x] = True
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        while q:
            tmp_y, tmp_x = q.popleft()
        
            if grid[tmp_y][tmp_x] != '0':
                is_connected[tmp_y][tmp_x] = True
                continue

            if not is_connected[tmp_y][tmp_x]:
                is_connected[tmp_y][tmp_x] = True

            for i in range(4):
                nx = tmp_x + dx[i]
                ny = tmp_y + dy[i]
                if is_valid_position(ny, nx) and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

    for request in requests:
        if len(request) == 1:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == request[0] and is_connected[i][j]:
                        grid[i][j] = '0'
                        answer -= 1
        else:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == request[0]:
                        grid[i][j] = '0'
                        answer -= 1

        visited = [ [False for _ in range(m)] for _ in range(n) ]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0' and is_connected[i][j]:
                    bfs(i, j, visited)
                                
    return answer