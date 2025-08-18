n, k = map(int, input().split())

nations = [ _ for _ in range(n) ]
for i in range(n):
    nation, gold, silver, bronze = map(int, input().split())
    nations[i] = (gold, silver, bronze)
    if nation == k:
        target = nations[i]

nations.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
result = nations.index(target) + 1
print(result)