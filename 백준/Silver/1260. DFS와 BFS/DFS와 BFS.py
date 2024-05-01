from collections import deque
from sys import stdin
input = stdin.readline

n, m, v = map(int, input().rstrip().split())
graph = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

for i in range(n):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v-1] = 1
    print(v, end=" ")
    for i in graph[v-1]:
        if visited[i-1] != 1:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start-1] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v-1]:
            if visited[i-1] != 1:
                q.append(i)
                visited[i-1] = 1

visited = [0 for i in range(n)]
dfs(graph, v, visited)
print()
visited = [0 for i in range(n)]
bfs(graph, v, visited)
print()