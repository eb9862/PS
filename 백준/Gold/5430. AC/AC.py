from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    p = list(input().rstrip())
    n = int(input().rstrip())
    arr = map(int, input().rstrip()[1:-1].split(","))
    if n != 0:
        arr = deque(arr)
    else:
        arr = deque([])

    brk = 0
    l = len(p)
    i = 0
    r = 0
    while i < l:
        if p[i] == "D":
            if n != 0:
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
                n -= 1
            else:
                print("error\n")
                brk = 1
                break
        else:
            r += 1
        i += 1
    
    if brk != 1:
        if r % 2 == 1:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]\n")