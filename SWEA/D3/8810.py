#당근밭 옆 고구마밭
import sys
sys.stdin = open('8810.txt')
# runtime
t = int(input())
for tc in range(1, t+1):
    dist = int(input()) # 10
    goguma = list(map(int,input().split()))
    li = []
    temp = 0
    cnt = 0
    while len(goguma) > 0:
        if goguma[0] < goguma[1] and len(goguma) != 1:
            if temp == 0: # 첫 시작
                temp += goguma[0]
                temp += goguma[1]
                cnt += 2
                goguma.pop(0)
            else: # 두번째 증가
                temp += goguma[1]
                cnt += 1
                goguma.pop(0)
        elif goguma[0] >= goguma[1] and len(goguma) != 1: # 감소구간
            goguma.pop(0) #이미 더한 앞껏만 빼버리고 혹은 계속 감소시 앞부분    
            if cnt >= 2:
                li.append([cnt,temp])
                cnt = 0
                temp = 0
        if len(goguma) == 1:
            if cnt >= 2:
                li.append([cnt,temp])
                break
            else:
                break
    li.sort(reverse=True)
    print('#{} {} {}'.format(tc, len(li), li[0][1]))
