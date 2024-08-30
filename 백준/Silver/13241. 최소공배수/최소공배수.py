a, b = map(int, input().split())

s1 = set()
s2 = set()

if a < 10:
    for i in range(1, a + 1):
        if a % i == 0:
            s1.add(i)
            s1.add(a//i)
else:
    for i in range(1, int(a/2) + 1):
        if a % i == 0:
            s1.add(i)
            s1.add(a//i)

if b < 10:
    for i in range(1, b + 1):
        if b % i == 0:
            s2.add(i)
            s2.add(b // i)
else:
    for i in range(1, int(b/2) + 1):
        if b % i == 0:
            s2.add(i)
            s2.add(b // i)

gcd = max(s1.intersection(s2))
print(a * b // gcd)