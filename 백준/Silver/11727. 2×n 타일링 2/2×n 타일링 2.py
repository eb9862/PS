n = int(input())
lst = [0 for i in range(n+3)]

lst[1] = 1
lst[2] = 3
lst[3] = 1 + 1 + 3

if n < 3:
    print(lst[n])
else:
    for i in range(3, n+1):
        lst[i] = lst[i - 2] * 2 + lst[i-1]
    print(lst[n] % 10007)