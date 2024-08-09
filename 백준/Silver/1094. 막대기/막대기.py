n = int(input())
binary = bin(n)[2:]
lst = [ int(i) for i in binary ]
print(sum(lst))