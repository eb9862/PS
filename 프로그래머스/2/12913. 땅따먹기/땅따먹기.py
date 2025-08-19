def solution(land):
    l = len(land)
    dp = [ [0, 0, 0, 0] for _ in range(l) ]

    dp[0] = land[0][:]
    
    for i in range(1, l):
        for j in range(4):
            can_step = [0, 1, 2, 3]
            can_step.remove(j)
            m = max([ dp[i-1][k] for k in can_step ])
            dp[i][j] = land[i][j] + m
    
    return max(dp[l-1])