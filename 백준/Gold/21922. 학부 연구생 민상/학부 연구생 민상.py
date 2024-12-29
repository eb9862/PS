def is_valid_coordinate(x: int, y: int) -> bool:
    global n, m
    if x < 0 or x >= m:
        return False
    if y < 0 or y >= n:
        return False
    return True
    
def change_direction(stuff: int, direction: tuple) -> tuple:
    global up, down, left, right
    
    if stuff == 4:
        if direction == up:
            return left
        elif direction == down:
            return right
        elif direction == right:
            return down
        else:
            return up
    
    if stuff == 3:
        if direction == up:
            return right
        elif direction == down:
            return left
        elif direction == right:
            return up
        else:
            return down

def can_move(stuff: int, direction: tuple) -> bool:
    if stuff == 1:
        if direction == left or direction == right:
            return False
    if stuff == 2:
        if direction == up or direction == down:
            return False
    return True

def count_seat(start_direction: tuple, seat: list, ac: tuple):
    global visited, result
    y = ac[0]
    x = ac[1]
    
    visited[y][x] = True
    direction = start_direction
    x += direction[0]
    y += direction[1]
    while is_valid_coordinate(x, y):
        if seat[y][x] == 9:
            return
        if visited[y][x] == False:
            visited[y][x] = True
            result += 1
        if seat[y][x] in [1, 2]:
            if not can_move(seat[y][x], direction):
                return
        if seat[y][x] in [3, 4]:
            direction = change_direction(seat[y][x], direction)
        x += direction[0]
        y += direction[1]


up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

n, m = map(int, input().split())
visited = [ [False for _ in range(m)] for _ in range(n) ]

seat = [[] for _ in range(n)]
ac_positions = []
for i in range(n):
    seat[i] = list(map(int, input().split()))
    if 9 in seat[i]:
        ac_cnt = seat[i].count(9)
        idx = 0
        for _ in range(ac_cnt):
            idx = seat[i].index(9, idx)
            ac_positions.append((i, idx))
            idx += 1

result = 0
for ac in ac_positions:
    count_seat(up, seat, ac)
    count_seat(down, seat, ac)
    count_seat(left, seat, ac)
    count_seat(right, seat, ac)
    result += 1

print(result)