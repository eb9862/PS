N = int(input())
n1 = 0
n2 = 0

while 3 * n1 < N:
    n1 += 1
n2 = n1

for i in range(n2, -1, -1):
    for j in range(n1, -1, -1):
        if (3 * j) + (5 * i) == N:
            print(i + j)
            exit()
print(-1)