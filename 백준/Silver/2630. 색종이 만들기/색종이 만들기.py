n = int(input())

papers = [ [] for _ in range(n)]
for i in range(n):
    papers[i] = list(map(int, input().split()))

result = [0, 0]

def can_cut(y: int, x: int, size: int, paper_color: int) -> bool:
    global papers

    for i in range(y, y + size):
        for j in range(x, x + size):
            if papers[i][j] != paper_color:
                return False
    return True

def check_recursive(y: int, x: int, size: int, paper_color: int):
    global result, papers
    
    if size == 1:
        if papers[y][x] == paper_color:
            result[paper_color] += 1
        return
    if can_cut(y, x, size, paper_color):
        result[paper_color] += 1
        return
    else:
        next_size = size // 2
        check_recursive(y, x, next_size, paper_color)
        check_recursive(y + next_size, x , next_size, paper_color)
        check_recursive(y, x + next_size, next_size, paper_color)
        check_recursive(y + next_size, x + next_size, next_size, paper_color)

check_recursive(0, 0, n, 0)
check_recursive(0, 0, n, 1)

print(result[0])
print(result[1])