n, k = map(int, input().split())

if n >= k:
    print(n - k)
    exit()

dp = [ float('inf') for _ in range(100001) ]
dp[n] = 0

for i in range(k+1):
    dp[i] = abs(i - n)

for i in range(n+1, k+1):
    if i % 2 == 0:
        cases = [ dp[i-1] + 1, dp[i // 2] + 1 ]
    else:
        cases = [ dp[i-1] + 1, dp[(i+1)// 2] + 2 ]
    dp[i] = min(cases)

print(dp[k])