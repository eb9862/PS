n = int(input())
lst = list(map(int, input().split()))

subtotal = [ 0 for _ in range(n)]
sum = 0
for i in range(n):
    sum += lst[i]
    subtotal[i] = sum
subtotal = [0] + subtotal

mn = subtotal[0]
res = []
for i in range(1, n+1):
    if mn > subtotal[i-1]:
        mn = subtotal[i-1]
    res.append(max(subtotal[i], subtotal[i] - mn))
print(max(res))