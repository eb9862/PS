n = int(input())

def hanoi(num: int, a: int, b: int, c: int):
    if num == 1:
        print(a, b)
        return

    hanoi(num - 1, a, c, b)
    print(a, b)
    hanoi(num - 1, c, b, a)

print(2**n - 1)
hanoi(n, 1, 3, 2)