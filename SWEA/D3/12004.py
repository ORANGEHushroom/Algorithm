import sys
sys.stdin = open('12004.txt')


t = int(input())
for tc in range(1, t+1):
    a = [1,2,3,4,5,6,7,8,9]
    n = int(input())
    flag = 0 # no
    for i in a:
        for j in a:
            if i*j == n:
                flag = 1
    if flag == 1:
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))

