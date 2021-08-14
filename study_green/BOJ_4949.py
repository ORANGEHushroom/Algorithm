
while True:
    #a = list(map(str,input().split()))
    a = input()
    if a.count('(') == a.count(')') and a.count('[') == a.count(']'):
        print('yes')
    elif  a.count('(') != a.count(')') or a.count('[') != a.count(']'):
        print('no')
    else:
        break    