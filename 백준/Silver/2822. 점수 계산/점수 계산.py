lst = [ [] for _ in range(8)]
for i in range(8):
    lst[i] = [int(input()), i + 1]

lst.sort(key=lambda x : x[0], reverse=True)

res = [ 0 for _ in range(5)]
score = 0
for i in range(5):
    score += lst[i][0]
    res[i] = lst[i][1]

print(score)
res.sort()
print(*res)