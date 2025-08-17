light_bulbs = input()
l = len(light_bulbs)
lb = [ True if light_bulbs[i] == 'Y' else False for i in range(l)]

result = 0
for i in range(l):
    if lb[i] == True:
        result += 1
        for j in range(i, l, i+1):
            lb[j] = not lb[j]

print(result)