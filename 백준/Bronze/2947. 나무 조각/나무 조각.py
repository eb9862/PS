order = list(map(int, input().split()))
n = len(order)

for i in range(n):
    for j in range(n-1):
        if order[j] > order[j+1]:
            order[j], order[j+1] = order[j+1], order[j]
            print(*order)