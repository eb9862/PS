n = int(input())
k = int(input())
recommends = list(map(int, input().split()))

frames = {} # 번호: [추천횟수, 게시 시간]

for i in range(k):
    r = recommends[i]
    if r in frames.keys():
        frames[r][0] += 1
    else:
        # 사진틀이 차있는 경우
        if len(frames.keys()) >= n:
            to_remove = sorted(frames.items(), key=lambda x: (x[1][0], x[1][1]))
            del frames[to_remove[0][0]]
        frames[r] = [1, i]
            
result = sorted(frames.keys())
print(*result)