n = int(input())
five = n // 5

if n == 1:
    print(-1)
    exit()
if n % 5 == 2 or n % 5 == 4:
    two = (n % 5) // 2
    print(five + two)
    exit()
elif n % 5 == 0:
    print(five)
    exit()
while five != 0:
    remain = n - (five * 5)
    if remain % 2 == 0:
        res = remain // 2 + five
        print(res)
        exit()
    five -= 1
if n % 2 != 0:
    print(-1)
else:
    print(n // 2)