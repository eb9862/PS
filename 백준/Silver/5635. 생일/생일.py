n = int(input())
lst = [ [] for _ in range(n)]
for i in range(n):
    lst[i] = list(input().split())
    for j in range(3):
        lst[i][j+1] = int(lst[i][j+1])

lst.sort(key=lambda x : (x[3], x[2], x[1]))
print(lst[-1][0])
print(lst[0][0])