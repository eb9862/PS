lst = list(map(int, input().split()))
k = lst[0]
lst.pop(0)
lst.sort()

def bt(n, arr):
    global lst
    if n == 6:
        print(*arr)
        return
    for i in lst:
        if n == 0:
            bt(n+1, arr + [i])
        elif n != 0 and arr[-1] < i:
            bt(n+1, arr + [i])

while k != 0:
    bt(0, [])
    print()
    lst = list(map(int, input().split()))
    k = lst[0]
    lst.pop(0)
    lst.sort()