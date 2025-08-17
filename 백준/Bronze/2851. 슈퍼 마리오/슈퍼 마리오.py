score = 0

for i in range(10):
    mushroom = int(input())
    if score + mushroom > 100:
        if abs(score - 100) >= abs(score + mushroom - 100):
            score += mushroom
        break
    score += mushroom

print(score)