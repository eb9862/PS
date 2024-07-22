N = int(input())
pinary = [0 for i in range(91)]
pinary[1] = 1
pinary[2] = 1
pinary[3] = 2

if N > 3:
    for i in range(4, N+1):
        pinary[i] = pinary[i-1] + pinary[i-2]
print(pinary[N])