from sys import stdin
input = stdin.readline

N = int(input().rstrip())
stairs = [ 0 for _ in range(N) ]
for i in range(N):
    stairs[i] = int(input().rstrip())

dp = [0 for _ in range(N)]

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    dp[2] = max(dp[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stairs[i], stairs[i] + stairs[i-1] + dp[i-3])

    print(dp[N-1])