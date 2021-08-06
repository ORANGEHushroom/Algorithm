while True:
    a = str(input())
    if a == a[::-1] and a != '0':
        print('yes')
    elif a != a[::-1] and a != '0':
        print('no')
    elif a == '0':
        break
    