from collections import deque

n = int(input())
prices = list(map(int, input().split()))
prices = deque(prices)
prices.appendleft(0)

dp = [ 0 for _ in range(n + 1)]
dp[1] = prices[1]

for i in range(2, n+1):
	dp[i] = max([ dp[j] + dp[i - j] for j in range(i // 2 + 1) ])
	dp[i] = max(dp[i], prices[i])

print(dp[n])