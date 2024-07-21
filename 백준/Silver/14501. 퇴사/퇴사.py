from sys import stdin
input = stdin.readline

N = int(input().rstrip())
t = [0 for i in range(N+1)]
p = [0 for i in range(N+1)]
for i in range(1, N+1):
    T, P = map(int, input().rstrip().split())
    t[i] = T
    p[i] = P

res = []
def cal_cost(t_lst, p_lst, i, cost):
    global N
    if i > N:
        res.append(cost)
        return
    if i + t_lst[i] - 1 > N:
        cal_cost(t_lst, p_lst, i+1, cost)
    else:
        cal_cost(t_lst, p_lst, i + t_lst[i], cost + p_lst[i])
        cal_cost(t_lst, p_lst, i+1, cost)

for j in range(1, N+1):
    cal_cost(t, p, j, 0)
print(max(res))