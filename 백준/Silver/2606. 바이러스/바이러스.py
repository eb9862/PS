from sys import stdin
input = stdin.readline

n = int(input().rstrip())
graph = [[] for i in range(n)]
c = int(input().rstrip())

for _ in range(c):
    a, b = map(int, input().rstrip().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

visited = [0 for i in range(n)]
def dfs(graph, v, visited):
    visited[v-1] = 1
    for i in graph[v-1]:
        if visited[i-1] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(sum(visited)-1)