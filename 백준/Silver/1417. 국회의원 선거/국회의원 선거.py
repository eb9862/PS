N = int(input())
votes = [ 0 for _ in range(N+1)]
for i in range(1, N+1):
    votes[i] = int(input())

if N == 1:
    print(0)
    exit()

res = 0
while True:
    brk = 1
    for i in range(2, N+1):
        if votes[1] <= votes[i]:
            brk = 0
    if brk == 1:
        break
    mx_idx = 2
    for i in range(2, N+1):
        if votes[mx_idx] < votes[i]:
            mx_idx = i
    votes[mx_idx] -= 1
    votes[1] += 1
    res += 1
print(res)