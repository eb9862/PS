n = int(input())
ascending_nums = [ {} for _ in range(n + 1)]

for i in range(10):
    ascending_nums[1][i] = 1 # [숫자 길이][마지막 숫자]

if n > 1:
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                ascending_nums[i][j] = ascending_nums[i-1][j]
            else:
                ascending_nums[i][j] = ascending_nums[i][j-1] + ascending_nums[i-1][j]

result = sum(ascending_nums[n].values()) % 10007
print(result)