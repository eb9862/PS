n, k = map(int, input().split())

coins = [ 0 for i in range(n) ]
cases = [ 0 for i in range(k + 1) ]
cases[0] = 1

for i in range(n):
    coins[i] = int(input())

for coin in coins:
    for i in range(coin, k + 1):
        cases[i] += cases[i - coin]

print(cases[k])