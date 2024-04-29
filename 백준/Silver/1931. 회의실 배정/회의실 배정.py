import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = [[] for _ in range(N)]
for i in range(N):
    lst[i] = list(map(int, input().rstrip().split()))

'''lst.sort()
lst.sort(key=lambda x: x[1])'''
lst.sort(key=lambda x : (x[1], x[0]))

cnt = 0
end = 0
for t in lst:
    if t[0] >= end:
        end = t[1]
        cnt += 1
print(cnt)