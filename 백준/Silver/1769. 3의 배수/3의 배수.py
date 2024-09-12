N = int(input())

if N <= 9:
    print(0)
    if N % 3 == 0:
        print("YES")
    else:
        print("NO")
    exit()
cnt = 1
val = 0
lst = list(str(N))
for i in lst:
    val += int(i)

while val // 10 != 0:
    lst = list(str(val))
    cnt += 1
    val = 0
    for i in lst:
        val += int(i)

print(cnt)
if val % 3 == 0:
    print("YES")
else:
    print("NO")