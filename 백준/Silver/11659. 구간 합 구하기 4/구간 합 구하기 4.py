from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N, M = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))

n_sum = [0 for _ in range(N + 1)]
n_sum[1] = lst[0]
n_sum[0] = 2
for _ in range(M):
    i, j = map(int, input().rstrip().split())
    
    if n_sum[j] == 0:
        for k in range(n_sum[0], j+1):
            n_sum[k] = n_sum[k-1] + lst[k-1]
        n_sum[0] = j
    
    res = n_sum[j] - n_sum[i] + lst[i-1]
    print(str(res) + '\n')