import sys
sys.stdin = open('11688.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc),end=' ')
    st = input()
    a = 1
    b = 1
    alpha = a / b
    for i in range(len(st)):
        if st[i] == 'L':
            alpha = a/(a+b)
            a = a
            b = a+b
        elif st[i] == 'R':
            alpha = (a+b)/b
            a = a+b
            b = b
    print(a,b)