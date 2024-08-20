import math
def is_prime(N):
    num = int(math.sqrt(N) + 1)
    for i in range(2, num):
        if N % i == 0:
            return 0
    return 1

T = int(input())
for _ in range(T):
    n = int(input())
    if n >= 0 and n <= 2:
        print(2)
    else:
        while True:
            if is_prime(n):
                print(n)
                break
            else:
                n += 1