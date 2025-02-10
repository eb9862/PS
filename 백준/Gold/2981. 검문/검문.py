import math

n = int(input())

numbers = [ 0 for _ in range(n) ]
for i in range(n):
    numbers[i] = int(input())

numbers.sort()

new_numbers = [ numbers[i+1] - numbers[i] for i in range(n-1)]
if n != 2:
    gcds = [ math.gcd(new_numbers[i], new_numbers[i+1]) for i in range(n-2)]
else:
    gcds = new_numbers

gcd_value = gcds[0]
for gcd in gcds:
    gcd_value = math.gcd(gcd_value, gcd)

def find_divisors(num: int) -> set:
    divisors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

divisors = find_divisors(gcd_value)
divisors = list(divisors)
divisors.sort()
divisors.remove(1)

print(*divisors)