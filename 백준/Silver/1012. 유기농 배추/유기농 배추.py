import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x, y):
        global m, n
        if x <= -1 or x > m-1 or y < 0 or y > n-1:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x+1, y)
            return True
        return False

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().rstrip().split())
    graph = [[0 for _ in range(m)] for i in range(n)]
    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        graph[y][x] = 1
    
    res = 0
    for i in range(n):
        for j in range(m):
            if dfs(j, i) == True:
                res += 1
    print(res)