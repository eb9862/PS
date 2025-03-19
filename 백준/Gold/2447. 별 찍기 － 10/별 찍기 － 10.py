n = int(input())

stars = [ [ True for _ in range(n)] for _ in range(n)]

def apply_pattern(y: int, x: int, num: int):
    blank = num // 3
    if num == 1:
        return
    
    for i in range(y + blank, y + 2*blank):
        for j in range(x + blank, x + 2*blank):
            stars[i][j] = False
    
    for i in range(y, y + num, blank):
        for j in range(x, x + num, blank):
            apply_pattern(i, j, blank)

apply_pattern(0, 0, n)
            
for i in range(n):
    for j in range(n):
        if stars[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    print()