from collections import deque

M, N, H = map(int, input().split())
boxes = [[[] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        boxes[i][j] = list(map(int, input().split()))

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

dq = deque([])
end = 0
for k in range(H):
    for j in range(N):
        for i in range(M):
            if boxes[k][j][i] == 1:
                dq.append((k, j, i))
            if boxes[k][j][i] == 0:
                end = 1
if end == 0:
    print(0)
    exit(0)

day = 0
first = len(dq)
second = 0
while dq:
    z, y, x = dq.popleft()
    visited[z][y][x] = True
    linked = [(z+1, y, x), (z-1, y, x), (z, y+1, x), (z, y-1, x), (z, y, x+1), (z, y, x-1)]
    for k, j, i in linked:
        if i >= 0 and i < M and j >= 0 and j < N and k >= 0 and k < H:
            if visited[k][j][i] != True:
                if boxes[k][j][i] == 0:
                    boxes[k][j][i] = 1
                    dq.append((k, j, i))
                    second += 1
                visited[k][j][i] = True
    first -= 1
    if first == 0:
        first = second
        second = 0
        day += 1

for k in range(H):
    for j in range(N):
        for i in range(M):
            if boxes[k][j][i] == 0:
                print(-1)
                exit(0)
print(day-1)