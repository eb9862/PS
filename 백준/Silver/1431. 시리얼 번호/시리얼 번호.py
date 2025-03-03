def sum_digits(x: int) -> int:
    result = 0
    if x.isalpha():
        return result

    for d in list(x):
        if d.isdigit():
            result += int(d)
    return result

n = int(input())

ids = [ _ for _ in range(n)]
for i in range(n):
    ids[i] = input()

ids.sort(key=lambda x: (len(x), sum_digits(x), x))

for id in ids:
    print(id)