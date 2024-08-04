from collections import deque

M, N = map(int, input().split())
box = [[] for _ in range(N)]
for i in range(N):
    box[i] = list(map(int, input().split()))

visited = [[False for _ in range(M)] for _ in range(N)]

dq = deque([])
end = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            dq.append((i, j))
        if box[i][j] == 0:
            end = 1

if end == 0:
    print(0)
    exit(0)

day = 0
first = len(dq)
second = 0
while dq:
    y, x = dq.popleft()
    visited[y][x] = True
    linked = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
    for i, j in linked:
        if i >= 0 and i < N and j >= 0 and j < M:
            if visited[i][j] != True:
                if box[i][j] == 0:
                    box[i][j] = 1
                    dq.append((i, j))
                    second += 1
                visited[i][j] = True
    first -= 1
    if first == 0:
        first = second
        second = 0
        day += 1

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
print(day-1)