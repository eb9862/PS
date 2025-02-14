def eratosthenes(num: int) -> list:
    is_prime = [True for _ in range(num+1)]
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, num + 1):
        if is_prime[i]:
            for j in range(i**2, num + 1, i):
                is_prime[j] = False
    
    return is_prime

t = int(input())

for _ in range(t):
    n = int(input())
    is_prime = eratosthenes(n)
    
    primes = [ i for i in range(2, n+1) if is_prime[i]]
    
    goldbach_partitions = set()
    for num in primes:
        if is_prime[n - num]:
            goldbach_partitions.add((min(num, n - num), max(num, n - num)))
    
    print(len(goldbach_partitions))