N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def bt(n, arr):
    global M, lst
    if n == M:
        print(*arr)
        return
    for i in lst:
        if n == 0:
            bt(n+1, arr + [i])
        elif i > arr[-1]:
            bt(n+1, arr + [i])

bt(0, [])