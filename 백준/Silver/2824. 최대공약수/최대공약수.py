import math

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

a = 1
for num in n_list:
    a *= num

b = 1
for num in m_list:
    b *= num

gcd = str(math.gcd(a, b))

if len(gcd) > 9:
    print(gcd[-9:])
else:
    print(gcd)