n, r, c = map(int, input().split())

size = 2**n
turn = 0

def is_target_quadrant(y: int, x: int, size: int) -> bool:
    global r, c
    
    if r in range(y, y+size) and c in range(x, x+size):
        return True
    return False

def move_z(y: int, x: int, size: int):
    global turn, r, c
    
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    
    if not is_target_quadrant(y, x, size):
        turn += size**2
        return
    
    if size == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny == r and nx == c:
                print(turn)
            turn += 1
        return
    
    new_size = size // 2
    dx = [0, new_size, 0, new_size]
    dy = [0, 0, new_size, new_size]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        move_z(ny, nx, new_size)

move_z(0, 0, size)