from sys import setrecursionlimit
setrecursionlimit(100000)
from sys import stdin
input = stdin.readline

def dfs_color(y, x, color):
    global map, visited1

    if y < 0 or y >= N or x < 0 or x >= N:
        return False
    if visited1[y][x] == False and map[y][x] == color:
        visited1[y][x] = True
        dfs_color(y, x-1, color)
        dfs_color(y, x+1, color)
        dfs_color(y-1, x, color)
        dfs_color(y+1, x, color)
        return True
    return False

def dfs_RG(y, x, color):
    global map, visited2
    
    if y < 0 or y >= N or x < 0 or x >= N:
        return False
    if color == 'R' or color == 'G':
        c = ['R', 'G']
    else:
        c = ['B']
    if visited2[y][x] == False and map[y][x] in c:
        visited2[y][x] = True
        dfs_RG(y, x-1, color)
        dfs_RG(y, x+1, color)
        dfs_RG(y-1, x, color)
        dfs_RG(y+1, x, color)
        return True
    return False

N = int(input().rstrip())

map = ['0' for _ in range(N)]
for i in range(N):
    map[i] = input().rstrip()

visited1 = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]

cnt1 = 0
cnt2 = 0
for j in range(N):
    for i in range(N):
        if dfs_color(j, i, map[j][i]) == True:
            cnt1 += 1
        if dfs_RG(j, i, map[j][i]) == True:
            cnt2 += 1

print(cnt1, cnt2)