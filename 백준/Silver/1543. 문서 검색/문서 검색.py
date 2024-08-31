s = input()
target = input()

l = len(s)
ll = len(target)

res = 0
i = 0
while i < l:
    if s[i] == target[0]:
        if i + ll < l + 1 and s[i:i+ll] == target:
            res += 1
            i += ll
        else:
            i += 1
    else:
        i += 1
print(res)