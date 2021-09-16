import sys
sys.stdin = open('12368.txt')

T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input().split())
    if a+b <= 23:
        print('#{} {}'.format(tc,a+b))

    else:
        print('#{} {}'.format(tc,a+b-24))