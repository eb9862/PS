n = int(input())

graph = [ [ False for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            graph[i][j] = True

result = [ [ 0 for _ in range(n)] for _ in range(n)]

def check_route(start: int, node: int):
    global visited, result
    
    if visited[node]:
        return
    
    visited[node] = True
    result[start][node] = 1
    for i in range(n):
        if graph[node][i]:
            check_route(start, i)

for i in range(n):
    visited = [ False for _ in range(n)]
    for j in range(n):
        if graph[i][j]:
            check_route(i, j)

for i in range(n):
    print(*result[i])