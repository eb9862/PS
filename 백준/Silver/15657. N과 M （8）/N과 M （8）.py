N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

res = []
def bt(lst, l):
    global M, nums, res
    if l == M:
        res.append(lst)
        return
    for i in nums:
        if l == 0:
            bt(lst + [i], l+1)
        else:
            if lst[-1] <= i:
                bt(lst + [i], l+1)

bt([], 0)
for case in res:
    print(*case)