from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(1, N+1):
    for l in combinations(lst, i):
        if sum(l) == S:
            res += 1
print(res)