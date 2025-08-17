n = int(input())

scores = [ 0 for _ in range(n) ]
for i in range(n):
    scores[i] = int(input())

result = 0
for i in range(n-2, -1, -1):
    if scores[i+1] <= scores[i]:
        sub = scores[i] - scores[i+1] + 1
        scores[i] -= sub
        result += sub

print(result)