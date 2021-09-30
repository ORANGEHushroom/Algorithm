import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1,t+1):
    print('#{}'.format(tc), end=" ")
    dem, lev, h = map(int,input().split())
    total = 0
    n = 0
    for i in range(h):
        total += dem * (1 + i * lev * 1/100)
    print(int(total))
    # while n>h:
    #     a = dem+ dem*n*lev*(0.01)
    #     total += a
    #     n +=1
    #     if n > h:
    #         break

    