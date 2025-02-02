import math, heapq

v, e = map(int, input().split())
start = int(input())

weights = [ {} for _ in range(v + 1)]

for _ in range(e):
    v1, v2, w = map(int, input().split())
    if v2 in weights[v1].keys():
        weights[v1][v2] = min(w, weights[v1][v2])
    else:
        weights[v1][v2] = w

d = [ float("inf") for _ in range(v+1)]
d[start] = 0

q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if dist > d[now]:
        continue
    for end, w in weights[now].items():
        cost = d[now] + w
        d[end] = min(d[end], cost)
        if d[end] == cost:
            heapq.heappush(q, (cost, end))

for i in range(1, v+1):
    if d[i] == float("inf"):
        print("INF")
    else:
        print(d[i])