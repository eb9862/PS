def solution(numbers):
    answer = 0
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1, l):
            mul = numbers[i] * numbers[j]
            answer = max(answer, mul)
    return answer