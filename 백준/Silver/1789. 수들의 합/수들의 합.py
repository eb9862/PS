S = int(input())

res = 0
for i in range(S+1):
    res += i
    if res == S:
        print(i)
        break
    elif res > S:
        print(i-1)
        break