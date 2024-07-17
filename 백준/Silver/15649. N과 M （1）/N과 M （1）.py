from itertools import permutations

N, M = map(int, input().split())

res = permutations([i for i in range(1, N+1)], M)
for i in res:
    case = list(i)
    print(*case)