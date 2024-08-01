s = input()
l = len(s)
flag = s[0]
zero = 0
one = 0
if flag == '0':
    zero += 1
else:
    one += 1

for i in range(l):
    if s[i] != flag:
        if s[i] == '0':
            zero += 1
            flag = '0'
        else:
            one += 1
            flag = '1'

if zero == 0 or one == 0:
    print(0)
else:
    print(min(zero, one))