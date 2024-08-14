N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [ False for _ in range(N+1)]

def dfs(n):
    global graph, visited, res
    if visited[n] == True:
        return 1
    visited[n] = True
    for v in graph[n]:
        dfs(v)
    return 0

if M == 0:
    print(N)
else:
    res = 0
    for i in range(1, N+1):
        if dfs(i) == 0:
            res += 1
    print(res)