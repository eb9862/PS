eq = input()
l = len(eq)

nums = []
opers = []
s = 0
for e in range(l):
    if (eq[e] == '+' or eq[e] == '-') and e != 0:
        opers.append(eq[e])
        nums.append(int(eq[s:e]))
        s = e + 1
nums.append(int(eq[s:]))

res = nums[0]
nums.remove(res)

l = len(nums)
i = 0
flag = 0
while i < l:
    if opers[i] == '-' and flag == 0:
        flag = 1
        res -= nums[i]
    elif opers[i] == '+' and flag == 1:
        res -= nums[i]
    elif opers[i] == '-' and flag == 1:
        flag == 0
        res -= nums[i]
    else:
        res += nums[i]
    i += 1
print(res)