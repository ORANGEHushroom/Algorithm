import sys
sys.stdin=open('carrot.txt')

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    size = list(map(int,input().split()))
    cnt = [1]
    sum_carrot = 1 # 초기값 3
    while len(size) > 0:
        if size[0] < size[1] and len(size) != 1:
            sum_carrot += 1
            size.pop(0)
        elif size[0] >= size[1] and len(size) != 1: # 감소
            size.pop(0)
            if sum_carrot != 1:
                cnt.append(sum_carrot)
                sum_carrot = 1
        if len(size) == 1:
            if sum_carrot != 1:
                cnt.append(sum_carrot)
                sum_carrot = 1
                break
            else:
                break
    print('#{} {}'.format(tc, max(cnt)))
