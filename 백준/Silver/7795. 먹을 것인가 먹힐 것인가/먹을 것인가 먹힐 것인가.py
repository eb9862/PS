T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    res = 0
    for i in A:
        for j in B:
            if i > j:
                res += 1
            else:
                break
    print(res)