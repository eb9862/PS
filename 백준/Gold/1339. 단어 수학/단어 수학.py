from collections import defaultdict

def get_order(words: list) -> list:
    weights = defaultdict(int)
    for word in words:
        for i in range(len(word) - 1, -1, -1):
            pos = len(word) - i
            weights[word[i]] += 10 ** (pos - 1)

    weights = sorted(weights.items(), key=lambda x: -x[1])
    order = [ x[0] for x in weights ]
    return order

def display_max_value(words: list, numbers: dict):
    result = 0
    sum_value = 0
    for word in words:
        value = word_to_number(word, numbers)
        sum_value += value
        if sum_value > result:
            result = sum_value
    print(result)

def word_to_number(word: str, numbers: dict) -> int:
    for key in numbers.keys():
        word = word.replace(key, numbers[key])
    return int(word)

n = int(input())

words = [ "" for i in range(n) ]

for i in range(n):
    words[i] = input()

order = get_order(words)

numbers = dict()
num = 9
for alpha in order:
    numbers[alpha] = str(num)
    num -= 1

display_max_value(words, numbers)