import math

n, s = map(int, input().split())

A = list(map(int, input().split()))

subs = [ abs(s - a) for a in A]

if n == 1:
    print(subs[0])
else:   
    print(math.gcd(*subs))