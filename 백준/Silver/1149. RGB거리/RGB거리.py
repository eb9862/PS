N = int(input())
lst = [ [] for _ in range(N) ]

for i in range(N):
    lst[i] = list(map(int, input().split()))

dp = [ [ 0 for _ in range(3)] for _ in range(N) ]
for i in range(3):
    dp[0][i] = lst[0][i]

for i in range(1, N):
    dp[i][0] = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = lst[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))