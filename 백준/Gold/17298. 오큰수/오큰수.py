n = int(input())
arr = list(map(int, input().split()))

stack = []
result = [ 0 for _ in range(n)]
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if not stack:
        result[i] = -1
    else:
        result[i]= stack[-1]
    stack.append(arr[i])

print(*result)