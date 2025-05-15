n = int(input())

wines = [ 0 for _ in range(n) ]
for i in range(n):
    wines[i] = int(input())

dp = [ 0 for _ in range(n) ]
if n >= 1:
    dp[0] = wines[0]
if n >= 2:
    dp[1] = wines[0] + wines[1]
if n >= 3:
    dp[2] = max(dp[0] + wines[2], wines[1] + wines[2], dp[1])
    for i in range(3, n):
        dp[i] = max(
            dp[i-2] + wines[i],
            dp[i-3] + wines[i-1] + wines[i],
            dp[i-1] # i번째를 마시지 않을 경우 <- 핵심..!
        )

print(max(dp))