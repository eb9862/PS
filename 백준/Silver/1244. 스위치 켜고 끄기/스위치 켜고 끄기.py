n = int(input())
status = list(map(int, input().split()))
k = int(input())

def toggle(idx: int):
    status[idx] = 1 - status[idx]

for i in range(k):
    gender, num = map(int, input().split())
    if gender == 1: # 남자
        for j in range(num - 1, n, num):
            toggle(j)
    else:
        toggle(num - 1)
        
        step = 1
        num -= 1
        while True:
            l = num - step
            r = num + step

            if l < 0 or r >= n:
                break
            
            if status[l] == status[r]:
                toggle(l)
                toggle(r)
            else:
                break

            step += 1

for i in range(0, n, 20):
    print(*status[i:i+20])