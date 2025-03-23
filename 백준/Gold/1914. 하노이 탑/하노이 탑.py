n = int(input())

k = 2**n - 1

def hanoi(num: int, start: int, dest: int, remain: int):
    if num == 1:
        print(start, dest)
        return
    
    hanoi(num - 1, start, remain, dest)
    print(start, dest)
    hanoi(num - 1, remain, dest, start)

print(k)
if n <= 20:
    hanoi(n, 1, 3, 2)