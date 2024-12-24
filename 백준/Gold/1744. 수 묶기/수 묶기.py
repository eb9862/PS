def is_natural_number(number: int) -> bool:
    if number <= 0:
        return False
    return True

n = int(input())

numbers = [ 0 for _ in range(n) ]
for i in range(n):
    numbers[i] = int(input())

numbers.sort()

cnt_natural_number = 0
for i in range(n):
    if is_natural_number(numbers[i]) == True:
        cnt_natural_number += 1

cnt_not_natural_number = n - cnt_natural_number

sum_value = 0
idx = 0
while idx < cnt_not_natural_number:
    if idx + 1 < cnt_not_natural_number:
        sum_value += numbers[idx] * numbers[idx+1]
    else:
        sum_value += numbers[idx]
    idx += 2

cnt_one = numbers.count(1)
idx = cnt_not_natural_number + cnt_one
sum_value += cnt_one

cnt_natural_number_witout_one = cnt_natural_number - cnt_one
if cnt_natural_number_witout_one % 2 != 0:
    sum_value += numbers[idx]
    idx += 1
while idx < n:
    if idx + 1 < n:
        sum_value += numbers[idx] * numbers[idx+1]
    idx += 2

print(sum_value)