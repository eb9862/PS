while True:
    try:
        n = int(input())
        res = 1
        num = '1'
        while int(num) % n != 0:
            res += 1
            num += '1'
        print(res)
    except:
        break