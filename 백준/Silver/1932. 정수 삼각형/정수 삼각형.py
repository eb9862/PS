n = int(input())
triangle = [[] for i in range(n)]

for i in range(n):
    triangle[i] = list(map(int, input().split()))

if n == 1:
    print(triangle[0][0])
    exit()

dp = [[0 for j in range(i+1)] for i in range(n)]
dp[0] = triangle[0]

for i in range(n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j];

print(max(dp[n-1]))