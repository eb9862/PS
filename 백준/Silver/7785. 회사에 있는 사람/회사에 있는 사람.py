from sys import stdin,stdout
input = stdin.readline
print = stdout.write

N = int(input().rstrip())
company = []
for _ in range(N):
    name, io = input().rstrip().split()
    if io == "enter":
        company.append(name)
    else:
        #if name in company:
            company.remove(name)

company.sort(reverse=True)
for p in company:
    print(p + "\n")