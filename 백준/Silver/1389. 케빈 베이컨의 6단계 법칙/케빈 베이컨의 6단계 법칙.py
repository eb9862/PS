n, m = map(int, input().split())

graph = [[ float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_value = float('inf')
result = 0
for i in range(n, 0, -1):
    sum_value = sum(graph[i][1:])
    if sum_value <= min_value:
        min_value = sum_value
        result = i

print(result)