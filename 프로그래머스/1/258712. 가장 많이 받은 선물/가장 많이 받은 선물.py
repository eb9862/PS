from collections import defaultdict

def calculate_gift_index(name: str, gifts: list) -> int:

    give = 0
    take = 0
    for gift in gifts:
        g, t = gift.split()
        if name == g:
            give += 1
        if name == t:
            take += 1
    return give - take

def calculate_give_and_take(name1: str, name2: str, gifts: list):

    give = 0
    take = 0
    for gift in gifts:
        g, t = gift.split()
        if g == name1 and t == name2:
            give += 1
        if g == name2 and t == name1:
            take += 1
    return give - take

def solution(friends, gifts):
    
    result = defaultdict(int)

    l = len(friends)
    for i in range(l):
        name = friends[i]
        for j in range(i+1, l):
            cnt = calculate_give_and_take(name, friends[j], gifts)
            if cnt > 0:
                result[name] += 1
            elif cnt < 0:
                result[friends[j]] += 1
            else:
                idx1 = calculate_gift_index(name, gifts)
                idx2 = calculate_gift_index(friends[j], gifts)
                if idx1 > idx2:
                    result[name] += 1
                elif idx1 < idx2:
                    result[friends[j]] += 1
    
    if result.values():
        return max(result.values())
    return 0