def solution(bandage, health, attacks):
    answer = 0
    
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    
    hp = health
    recovery = 0
    time = 1
    l = len(attacks)
    for i in range(l):
        while attacks[i][0] != time:
            # 체력 회복
            hp = min(hp + x, health)
            recovery += 1
            if recovery == t:
                hp = min(hp + y, health)
                recovery = 0
            time += 1
        # 공격 받음
        damage = attacks[i][1]
        hp -= damage
        recovery = 0
        if hp < 1:
            return -1
        time += 1
    answer = hp
    return answer