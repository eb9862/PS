import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())
a = [[] for _ in range(N)]
for i in range(N):
    a[i] = list(map(int, input().rstrip().split()))

M, K = map(int, input().rstrip().split())
b = [[] for _ in range(M)]
for i in range(M):
    b[i] = list(map(int, input().rstrip().split()))

bt = [[0 for _ in range(M)] for _ in range(K)]
for i in range(K):
    for j in range(M):
        bt[i][j] = b[j][i]

for lst1 in a:
    res = ""
    for lst2 in bt:
        ans = 0
        for i in range(M):
            ans += (lst1[i] * lst2[i])
        res += str(ans)
        res += " "
    print(res + '\n')