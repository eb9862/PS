def is_valid_coor(ny: int, nx: int, y: int, x: int) -> bool:
    if (0 <= ny and ny < y) and (0 <= nx and nx < x):
        return True
    return False

def solution(board, h, w):
    answer = 0
    
    y = len(board)
    x = len(board[0])
    color = board[h][w]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        if is_valid_coor(ny, nx, y, x) and board[ny][nx] == color:
            answer += 1
    return answer