from collections import deque
import math
from sys import stdin
input = stdin.readline

def nearest_node():
    min = math.inf
    node = 0
    for i in range(1, n + 1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            node = i
    return node

n = int(input().rstrip())
m = int(input().rstrip())

graph = [ {} for i in range(n + 1) ]
for i in range(m):
    bus_info = list(map(int, input().rstrip().split()))
    start = bus_info[0]
    end = bus_info[1]
    cost = bus_info[2]
    if end in graph[start].keys():
        if graph[start][end] > cost:
            graph[start][end] = cost
    else:
        graph[start][end] = cost
start, end =  map(int, input().rstrip().split())

distance = [ math.inf for i in range(n + 1) ]
visited = [ False for i in range(n + 1) ]

distance[start] = 0
visited[start] = True

for end_and_cost in graph[start].items():
    distance[end_and_cost[0]] = end_and_cost[1]

now = start
for i in range(n-1):
    now = nearest_node()
    visited[now] = True
    for end_and_cost in graph[now].items():
        cost = distance[now] + end_and_cost[1]
        if cost < distance[end_and_cost[0]]:
            distance[end_and_cost[0]] = cost

print(distance[end])
