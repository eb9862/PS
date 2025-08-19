def solution(emergency):
    answer = []
    copy = emergency[:]
    copy.sort(reverse=True)
    for e in emergency:
        rank = copy.index(e) + 1
        answer.append(rank)
    return answer