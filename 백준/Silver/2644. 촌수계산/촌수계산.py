n = int(input())
t1, t2 = map(int, input().split())
m = int(input())

graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [ False for _ in range(n+1) ]

def dfs(n, step):
    global visited, graph, t2, res
    if visited[n] == True:
        return
    visited[n] = True
    if n == t2:
        res.append(step)
        return
    for i in graph[n]:
        dfs(i, step+1)

res = []
dfs(t1, 0)
if res == []:
    print(-1)
else:
    print(min(res))