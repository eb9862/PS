from sys import stdin
input = stdin.readline

def is_valid_coor(y: int, x: int) -> bool:
    global n, m
    
    if y < 0 or y >= n:
        return False
    if x < 0 or x >= m:
        return False
    return True

def move_like_tetromino(y: int, x: int, move_count: int, sum_value: int):
    global visited, result
    
    if move_count == 4:
        result = max(sum_value, result)
        return
    
    visited[y][x] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_valid_coor(ny, nx) and not visited[ny][nx]:
            visited[ny][nx] = True
            move_like_tetromino(ny, nx, move_count + 1, sum_value + board[y][x])
            visited[ny][nx] = False

def move_like_T(y: int, x: int):
    global n, m, result
    
    if x+2 < m: # ㅗ, ㅜ
        bar = 0
        for i in range(3):
            bar += board[y][x+i]
        
        if is_valid_coor(y-1, x+1):
            sum_value = bar + board[y-1][x+1]
            if result < sum_value:
                result = sum_value

        if is_valid_coor(y+1, x+1):
            sum_value = bar + board[y+1][x+1]
            if result < sum_value:
                result = sum_value
    
    if y+2 < n: # ㅏ, ㅓ
        bar = 0
        for i in range(3):
            bar += board[y+i][x]
        
        if is_valid_coor(y+1, x+1):
            sum_value = bar + board[y+1][x+1]
            if result < sum_value:
                result = sum_value

        if is_valid_coor(y+1, x-1):
            sum_value = bar + board[y+1][x-1]
            if result < sum_value:
                result = sum_value

n, m = map(int, input().rstrip().split())

board = [ [] for _ in range(n) ]
for i in range(n):
    board[i] = list(map(int, input().rstrip().split()))

result = float("-inf")
visited = [ [ False for _ in range(m)] for _ in range(n)]

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        move_like_tetromino(y, x, 0, 0)
        visited[y][x] = False
        move_like_T(y, x)

print(result)