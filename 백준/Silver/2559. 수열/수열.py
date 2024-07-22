N, K = map(int, input().split())
lst = list(map(int, input().split()))
prefix_sum = [0 for _ in range(N+1)]
s = 0
for i in range(N):
    s += lst[i]
    prefix_sum[i+1] = s

mx = []
for i in range(N-K+1):
    t = prefix_sum[i+K] - prefix_sum[i]
    mx.append(t)
print(max(mx))