n = int(input())
arr = list(map(int, input().split()))

dp = [ n for n in arr]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + arr[i], dp[i])

print(max(dp))