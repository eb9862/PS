n = int(input())
towers = list(map(int, input().split()))

result = [ 0 for _ in range(n) ]
stack = [(0, 0)] # index, h
for i in range(n):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if not stack:
        result[i] = 0
    else:
        result[i] = stack[-1][0]
    stack.append((i + 1, towers[i]))

print(*result)