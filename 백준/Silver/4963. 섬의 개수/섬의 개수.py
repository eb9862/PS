import sys
input = sys.stdin.readline

def dfs_island(x, y):
    global w, h, graph
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs_island(x, y-1)
        dfs_island(x, y+1)
        dfs_island(x-1, y)
        dfs_island(x+1, y)
        dfs_island(x-1, y-1)
        dfs_island(x+1, y-1)
        dfs_island(x-1, y+1)
        dfs_island(x+1, y+1)
        return True
    return False

while (1):
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        exit()
    graph = [[] for i in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().rstrip().split()))

    cnt = 0
    for y in range(h):
        for x in range(w):
            if dfs_island(x, y) == True:
                cnt += 1
    print(cnt)