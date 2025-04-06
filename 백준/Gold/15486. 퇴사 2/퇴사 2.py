n = int(input())
period_and_cost = [ 0 for _ in range(n) ]

for i in range(n):
    period_and_cost[i] = list(map(int, input().split()))

dp = [ 0 for _ in range(n+1) ]
for i in range(n):
    period = period_and_cost[i][0]
    dp[i + 1] = max(dp[i], dp[i+1])
    if i + period < n + 1:
        dp[i+period] = max(dp[i + period], dp[i] + period_and_cost[i][1])

print(dp[-1])