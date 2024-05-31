from sys import stdin
input = stdin.readline

T = int(input().rstrip())
for _ in range(T):
    k = int(input().rstrip())
    n = int(input().rstrip())
    
    lst = [ [i+1 for i in range(n)] for _ in range(k+1)]
    
    for i in range(1, k + 1):
        for j in range(n):
            lst[i][j] = sum(lst[i-1][:j+1])
    
    print(lst[k][n-1])