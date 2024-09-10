N = int(input())

dp = [ [0 for _ in range(10)] for _ in range(N+1) ]

dp[1] = [0] + [1] * 9
for i in range(2, N+1):
    for k in range(10):
        if k == 0:
            dp[i][k] = dp[i-1][k+1]
        elif k == 9:
            dp[i][k] = dp[i-1][k-1]
        else:
            dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]

print(sum(dp[N]) % 1000000000)