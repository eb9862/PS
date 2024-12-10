import math

def dfs_mine(x : int, y: int):
    global N, M, soldiers, mine, visited_mine
    if not (0 <= x and x < N):
        return
    if not (0 <= y and y < M):
        return
    if visited_mine[y][x] == True:
        return
    
    visited_mine[y][x] = True
    if soldiers[y][x] == "W":
        mine += 1
    else:
        return
    
    dfs_mine(x-1, y)
    dfs_mine(x+1, y)
    dfs_mine(x, y-1)
    dfs_mine(x, y+1)
    
def dfs_enemies(x : int, y: int):
    global N, M, soldiers, enemies, visited_enemies
    if not (0 <= x and x < N):
        return
    if not (0 <= y and y < M):
        return
    if visited_enemies[y][x] == True:
        return
    
    visited_enemies[y][x] = True
    if soldiers[y][x] == "B":
        enemies += 1
    else:
        return
    
    dfs_enemies(x-1, y)
    dfs_enemies(x+1, y)
    dfs_enemies(x, y-1)
    dfs_enemies(x, y+1)

N, M = map(int, input().split())

soldiers = ['' for i in range(M)]

for i in range(M):
    soldiers[i] = input()

result = [0, 0]

visited_mine = [ [ False for i in range(N) ] for j in range(M) ]
visited_enemies = [ [ False for i in range(N) ] for j in range(M) ]

for y in range(M):
    for x in range(N):
        mine = 0
        dfs_mine(x, y)
        result[0] += int(math.pow(mine, 2))
        
        enemies = 0
        dfs_enemies(x, y)
        result[1] += int(math.pow(enemies, 2))

print(result[0], result[1])