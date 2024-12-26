n = int(input())

numbers = [ 0.0 for _ in range(n) ]
for i in range(n):
    numbers[i] = float(input())

dp = [ 0.0 for _ in range(n) ]

dp[0] = numbers[0]
for i in range(1,n):
    dp[i] = max(numbers[i], dp[i-1] * numbers[i])

print(f"{max(dp):.3f}")
