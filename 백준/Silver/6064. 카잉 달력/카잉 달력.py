t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    max_turn = m * n

    turn = x
    is_valid = False
    while turn <= max_turn:

        if turn % n == y % n:
            is_valid = True
            break

        turn += m
    
    if is_valid:
        print(turn)
    else:
        print(-1)