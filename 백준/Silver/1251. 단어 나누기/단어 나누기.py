word = input()
l = len(word)

lst = []

for i in range(1, l):
    for j in range(i+1, l):
        wrd1 = word[:i]
        wrd2 = word[i:j]
        wrd3 = word[j:]
        lst.append(wrd1[::-1] + wrd2[::-1] + wrd3[::-1])

lst.sort()
print(lst[0])