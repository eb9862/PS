n = int(input())
equation = list(input())

operands = [ 0 for _ in range(n)]
for i in range(n):
    operands[i] = int(input())

stack = []

def calculate(operator: str, x: float, y: float) -> float:
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    else:
        return x / y

for e in equation:
    if e.isalpha():
        index = ord(e) - ord('A')
        stack.append(operands[index])
    else:
        y = stack.pop()
        x = stack.pop()
        result = calculate(e, x, y)
        stack.append(result)

print(f"{stack[0]:.2f}")