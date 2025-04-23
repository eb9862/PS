n = int(input())
dp = [ 0 for _ in range(n+1) ] # [최대 개수, 버퍼에 복사된 개수]

for i in range(1, n+1):
    dp[i] = dp[i-1] + 1
    for j in range(3, i+1):
        dp[i] = max(dp[i], dp[i-j] * (j-1))

print(dp[-1])