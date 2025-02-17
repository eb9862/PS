import math

def solution(r1, r2):
    answer = 0
    
    answer += r2 - r1 + 1
    for x in range(1, r2+1):
        if r1**2 - x**2 < 0:
            min_y = 0
        else:
            min_y = math.sqrt(r1**2 - x**2)
        max_y = math.sqrt(r2**2 - x**2)   
        answer += math.floor(max_y) - math.ceil(min_y) + 1
        if min_y == 0:
            answer -= 1
    
    return answer * 4