import math

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

c1 = a1 * b2 + b1 * a2
c2 = a2 * b2

g = math.gcd(c1, c2)
while g != 1:
    c1 //= g
    c2 //= g
    g = math.gcd(c1, c2)

print(c1, c2)