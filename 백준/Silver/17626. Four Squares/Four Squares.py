import math

n = int(input())

root = int(math.sqrt(n))
if root**2 == n:
    print(1)
    exit()

squares = [ 0 for _ in range(n+1)]

for i in range(1, n+1):

    root = int(math.sqrt(i))
    if root**2 == n:
        squares[i] = 1
    else:
        squares[i] = float('inf')
        for j in range(1, root + 1):
            squares[i] = min(squares[i], squares[i - j**2] + 1)
            
print(squares[-1])