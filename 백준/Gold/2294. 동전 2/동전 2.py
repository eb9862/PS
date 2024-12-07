n, k = map(int, input().split())

dp = [0 for i in range(k+1)]
coins = [0 for i in range(n)]

for i in range(n):
    coins[i] = int(input())

for coin in coins:
    if coin <= k:
        dp[coin] = 1

for i in range(k+1):
    for j in range(i+1):
        if dp[i] != 0:
            if dp[j] != 0 and dp[i-j] != 0:
                dp[i] = min(dp[i], dp[j] + dp[i - j])
        else:
            if dp[j] != 0 and dp[i-j] != 0:
                dp[i] = dp[j] + dp[i - j]

if dp[k] == 0:
    print(-1)
else:
    print(dp[k])