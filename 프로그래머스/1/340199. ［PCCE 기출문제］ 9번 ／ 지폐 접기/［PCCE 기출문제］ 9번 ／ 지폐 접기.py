def can_finish(wallet, w, h) -> bool:
    if wallet[0] >= w and wallet[1] >= h:
        return True
    if wallet[0] >= h and wallet[1] >= w:
        return True
    return False

def solution(wallet, bill):
    fold = 0

    w = bill[0]
    h = bill[1]

    can_fold = True
    while can_fold:
        if can_finish(wallet, w, h):
            can_fold = False
        else:
            fold += 1
        if w < h:
            h //= 2
        else:
            w //= 2
        
    return fold

