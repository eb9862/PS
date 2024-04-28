s = input()

res = ""
l = len(s)
i = 0
while i < l:
    if s[i] == '<':
        while s[i] != '>':
            res += s[i]
            i += 1
        res += s[i]
        i += 1
    else:
        tmp = ""
        while i < l and s[i] != '<' and s[i] != ' ':
            tmp += s[i]
            i += 1
        res += tmp[::-1]
    if i < l and s[i] == ' ':
        res += ' '
        i += 1

print(res)