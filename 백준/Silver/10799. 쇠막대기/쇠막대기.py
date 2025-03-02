ip = input()
answer = 0

stack = []
l = len(ip)
i = 0
while i < l:
    if ip[i] == '(':
        if ip[i+1] != ')':
            stack.append(ip[i])
        elif ip[i+1] == ')':
            rod_num = len(stack)
            answer += rod_num
            i += 1
    else:
        stack.pop()
        answer += 1
    i += 1
print(answer)