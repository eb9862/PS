N = int(input())
lst = [0 for i in range(N)]
for i in range(N):
    lst[i] = int(input())

res = []
lst.sort(reverse=True)
for i in range(N):
    res.append(lst[i] * (i + 1))

print(max(res))