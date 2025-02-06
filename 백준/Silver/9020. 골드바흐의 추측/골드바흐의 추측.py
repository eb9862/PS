def eratosthenes(num: int) -> list:
    primes = [ True for _ in range(num + 1)]

    for i in range(2, num + 1):
        if primes[i]:
            for j in range(i**2, num + 1, i):
                    primes[j] = False
    
    return primes

t = int(input())

for _ in range(t):
    n = int(input())
    prime = eratosthenes(n)

    half = n // 2
    if prime[half] == True:
        print(half, half)
        continue

    prime_numbers = [ i for i in range(2, n + 1) if prime[i]]
    l, r, length = 0, 0, len(prime_numbers)
    for i in range(length):
        if prime_numbers[i] > half:
            l = i - 1
            r = i
            break
    
    while l >= 0 and r < length:
        sum_value = prime_numbers[l] + prime_numbers[r]
        if sum_value < n:
            r += 1
        elif sum_value > n:
            l -= 1
        else:
            print(prime_numbers[l], prime_numbers[r])
            break