def validate_input_string(bracket_string):
    stack = []
    l = len(bracket_string)
    for i in range(l):
        c = bracket_string[i]
        if c in ['(', '[']:
            stack.append(c)
        else:
            if not check_valid_pair(c, stack):
                print(0)
                exit()
    if stack:
        print(0)
        exit()

def check_valid_pair(c, stack):
    if stack:
        bracket = stack.pop()
        if c == ')' and bracket == '(':
            return True
        if c == ']' and bracket == '[':
            return True
    return False

def multiply_mul(c, mul):
    if c == '(':
        return mul * 2
    else:
        return mul * 3

def divide_mul(bracket, mul):
    if (bracket == '('):
        return mul // 2
    else:
        return mul // 3

bracket_string = input()
validate_input_string(bracket_string)

new_string = bracket_string.replace("()", "2");
new_string = new_string.replace("[]", "3");

stack = []
sum = 0
mul = 1
l = len(new_string)
for i in range(l):
    c = new_string[i]
    if c in ['(', '[']:
        stack.append(c)
        mul = multiply_mul(c, mul)
    elif c in ['2', '3']:
        sum += (mul * int(c))
    else:
        bracket = stack.pop()
        mul = divide_mul(bracket, mul)

print(sum)
