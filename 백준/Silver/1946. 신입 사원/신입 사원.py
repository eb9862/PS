t = int(input())
for _ in range(t):

    n = int(input())
    grades = [ 0 for _ in range(n) ]
    for i in range(n):
        grades[i] = list(map(int, input().split()))
    
    grades.sort()
    
    result = 0
    rank = grades[0][1]
    for i in range(n):
        if rank >= grades[i][1]:
            result += 1
            rank = grades[i][1]

    print(result)