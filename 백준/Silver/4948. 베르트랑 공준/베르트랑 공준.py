import math
n = int(input())

def is_prime(num):
    end = int(math.sqrt(num) + 1)
    for i in range(2, end):
        if num % i == 0:
            return -1
    return 0

while n != 0:
    l = 0
    for i in range(n+1, 2*n+1):
        if is_prime(i) == 0:
            l += 1
    print(l)
    n = int(input())