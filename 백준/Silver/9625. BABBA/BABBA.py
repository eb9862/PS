K = int(input())
a = 1
b = 0
for _ in range(K):
    new_b = a + b
    new_a = b
    a = new_a
    b = new_b
print(a, b)