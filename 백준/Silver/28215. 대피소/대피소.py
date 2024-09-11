from itertools import combinations

N, K = map(int, input().split())
houses = [[] for _ in range(N)]
for i in range(N):
    houses[i] = list(map(int, input().split()))

def cal_distance(p1, p2):
    sub_x = abs(p1[0] - p2[0])
    sub_y = abs(p1[1] - p2[1])
    return sub_x + sub_y

def d_nearer_shelter(house, shelters):
    d = []
    for p in shelters:
        d.append(cal_distance(house, p))
    return min(d)

cases = combinations(range(N), K)
res = 200000
for i in list(cases):
    shelters = []
    for x in range(K):
        shelters.append(houses[i[x]])
    ds = []
    for p in houses:
        d = d_nearer_shelter(p, shelters)
        if d != 0:
            ds.append(d)
    mx = max(ds)
    if res > mx:
        res = mx
print(res)