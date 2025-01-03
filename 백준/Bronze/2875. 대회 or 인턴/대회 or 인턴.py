n, m, k = map(int, input().split())

if n + m == k:
    print(0)
    exit()

teams = min(n // 2, m)
n -= teams * 2
m -= teams

if n + m >= k:
    print(teams)
    exit()

k -= n + m
while k > 0:
    teams -= 1
    k -= 3

print(teams)