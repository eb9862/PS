n, k = map(int, input().split())
num = input()

stack = []

for i in range(n):
    while stack and stack[-1] < num[i] and k > 0:
        stack.pop()
        k -= 1
    stack.append(num[i])

result = "".join(stack)
if k > 0:
    result = result[:-k]
print(result)