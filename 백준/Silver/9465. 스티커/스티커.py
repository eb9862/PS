t = int(input())

for _ in range(t):
    n = int(input())
    sticker0 = list(map(int, input().split()))
    sticker1 = list(map(int, input().split()))

    dp = [ [ 0 for _ in range(n)] for _ in range(2)] # 해당 위치의 스티커를 선책했을 때의 최대 가격
    dp[0][0] = sticker0[0]
    dp[1][0] = sticker1[0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = dp[1][0] + sticker0[1]
    dp[1][1] = dp[0][0] + sticker1[1]
    
    for i in range(2, n):
        dp[0][i] = sticker0[i] + max(dp[1][i-1], max(dp[0][i-2], dp[1][i-2]))
        dp[1][i] = sticker1[i] + max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2]))
    
    print(max(max(dp[0]), max(dp[1])))