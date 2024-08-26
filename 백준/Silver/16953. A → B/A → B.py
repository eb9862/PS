A, B = map(int, input().split())

res = []
def cal(num, l):
    global B
    if num >= B:
        if num == B:
            res.append(l)
        return
    cal(num*2, l+1)
    cal(int(str(num) + '1'), l+1)

cal(A, 1)
if res == []:
    print(-1)
else:
    print(min(res))