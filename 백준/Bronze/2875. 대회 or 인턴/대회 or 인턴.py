n, m, k = map(int, input().split())

teams = min(n // 2, m)
n -= teams * 2
m -= teams

k -= n + m
while k > 0:
    teams -= 1
    k -= 3

print(teams)