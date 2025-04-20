def is_valid_coor(y: int, x: int, r: int, c: int) -> bool:
    if 0 <= y and y < r and 0 <= x and x < c:
        return True
    return False

def check_mats(park, mats: list, y: int, x: int) -> int:
    
    r = len(park)
    c = len(park[0])
    
    answer = -1
    for size in mats:
        for i in range(size):
            for j in range(size):
                if not is_valid_coor(y+i, x+j, r, c) or park[y+i][x+j] != "-1":
                    return answer
        answer = size
    return answer

def solution(mats, park):
    answer = -1
    
    r = len(park)
    c = len(park[0])
    mats.sort()
    
    for i in range(r):
        for j in range(c):
            if park[i][j] == "-1":
                mat = check_mats(park, mats, i, j)
                if answer == -1:
                    answer = mat
                else:
                    answer = max(answer, mat)
    
    return answer