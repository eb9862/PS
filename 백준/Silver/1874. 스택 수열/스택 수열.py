from collections import deque

n = int(input())

number = 1
expected = deque([ 0 for _ in range(n)])
for i in range(n):
    expected[i] = int(input())

answer = []
pushes = []
can_make = True
while expected:
    
    if pushes and pushes[-1] == expected[0]:
        answer.append("-")
        pushes.pop()
        expected.popleft()
    elif number <= expected[0]:
        answer.append("+")
        pushes.append(number)
        number += 1
    else:
        can_make = False
        break

if not can_make:
    print("NO")
else:
    for op in answer:
        print(op)