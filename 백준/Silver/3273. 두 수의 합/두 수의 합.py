n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()

l = 0
r = n-1
res = 0
while l < r:
    if lst[r] > x - lst[l]:
        r -= 1
    elif lst[r] == x - lst[l]:
        res += 1
        l += 1
    else:
        l += 1
print(res)