# 당근밭 옆 고구마밭
'''
input
4
8
1 2 3 4 5 1 2 3
7
1 2 3 4 3 2 1
9
1 2 3 2 3 4 1 2 3
5
1 9 1 2 3
>> output
#1 2 15
#2 1 10
#3 3 9
#4 2 6
# '''
import sys
sys.stdin = open('8810.txt')

t = int(input())
for tc in range(1, t+1):
    dist = int(input()) # 10
    goguma = list(map(int,input().split()))
    li = []
    cnt = 0
    for i in range(len(goguma)): #0~9
        a = 0
        temp = goguma[0]
        while len(goguma) > 0:
            if goguma[a] < goguma[a+1] and a+1 <= len(goguma)-1: #0~9
                temp += goguma[a+1]
                
                a+=1
            elif goguma[a] >= goguma[a+1] and a+1 <= len(goguma)-1:
                if temp == goguma[0]:
                    break
                else:
                    li.append(temp)
                    cnt+=1
                    if a+1 <= len(goguma) -1:
                        goguma = goguma[a+1:]
                        
                    else:
                        goguma = [] 
                        break
    print('#{} {} {}'.format(tc, cnt, max(li)))
