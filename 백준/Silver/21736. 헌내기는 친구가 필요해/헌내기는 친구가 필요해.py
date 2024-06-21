N, M = map(int, input().split())
lst = [[] for _ in range(N)]
for i in range(N):
    lst[i] = input()

cnt = 0
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    if "I" in lst[i]:
        y = i
        x = lst[i].index("I")
        break

q = []
q.append((y,x))

for cor in q:
    if cor[0] < 0 or cor[0] >= N:
        continue
    if cor[1] < 0 or cor[1] >= M:
        continue
    if visited[cor[0]][cor[1]] == 1:
        continue
    
    visited[cor[0]][cor[1]] = 1
    if lst[cor[0]][cor[1]] == "X":
        continue
    elif lst[cor[0]][cor[1]] == "P":
        cnt += 1
    else:
        pass
    
    q.append((cor[0]-1, cor[1]))
    q.append((cor[0]+1, cor[1]))
    q.append((cor[0], cor[1]-1))
    q.append((cor[0], cor[1]+1))

if cnt != 0:
    print(cnt)
else:
    print("TT")