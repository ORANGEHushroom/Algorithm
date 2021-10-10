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
    root = 0
    temp = goguma[0]
    for i in range(len(goguma)-1):
        if goguma[i] < goguma[i+1]:
            temp += goguma[i+1]
    print(temp)
        



    print('#{} {}'.format(tc, root))
