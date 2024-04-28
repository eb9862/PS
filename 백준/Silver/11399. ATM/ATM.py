N = int(input())
lst = list(map(int, input().split()))
lst.sort()
num = 0
for i in range(N):
    num += lst[i] * (N - i)
print(num)