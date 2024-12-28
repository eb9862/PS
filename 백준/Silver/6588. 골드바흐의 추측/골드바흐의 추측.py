max_number = 1000000
eratosthenes_sieve = [ True for _ in range(max_number + 1) ]

for i in range(2, max_number + 1):
    if eratosthenes_sieve[i] == True:
        start = i**2
        for j in range(start, max_number + 1, i):
            eratosthenes_sieve[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    goldbach = False
    end = n // 2 + 1
    for a in range(3, end, 2):
        b = n - a
        if eratosthenes_sieve[b] and eratosthenes_sieve[a]:
            print(f"{n} = {a} + {b}")
            goldbach = True
            break
    if not goldbach:
        print("Goldbach's conjecture is wrong.")