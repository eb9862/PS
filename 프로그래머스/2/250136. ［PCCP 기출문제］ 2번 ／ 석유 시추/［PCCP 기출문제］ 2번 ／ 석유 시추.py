from collections import deque

def solution(land):
    answer = 0
    
    row = len(land)
    col = len(land[0])
    
    def can_move(y: int, x: int) -> bool:
        return (0 <= y and y < row) and (0 <= x and x < col)
    
    def find_points_to_move(y: int, x: int) -> list:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        points = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if can_move(ny, nx):
                points.append((ny, nx))
        return points
    
    def bfs(land: list, y: int, x: int):
    
        visited[y][x] = True
        q = deque([(y, x)])

        result = 0
        cols = set()
        while q:
            y, x = q.popleft()
            cols.add(x)
            result += 1

            points = find_points_to_move(y, x)

            for y, x in points:
                if not visited[y][x]:
                    visited[y][x] = True
                    if land[y][x] == 1:
                        q.append((y, x))
        return cols, result
    
    oils = [ 0 for _ in range(col)]
    visited = [ [False for _ in range(col)] for _ in range(row)]
    for y in range(row):
        for x in range(col):
            if land[y][x] == 1 and not visited[y][x]:
                cols, quantity = bfs(land, y, x)
                for c in cols:
                    oils[c] += quantity
    
    return max(oils)