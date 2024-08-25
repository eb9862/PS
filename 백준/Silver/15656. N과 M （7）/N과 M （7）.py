N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def bt(l, arr):
    global M, lst
    if l == M:
        print(*arr)
        return
    for i in lst:
        bt(l + 1, arr + [i])

bt(0, [])