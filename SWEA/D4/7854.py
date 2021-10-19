import sys
sys.stdin = open('7854.txt')

# python 문제가 아님
t = int(input())
for tc in range(1, t+1):
    a = int(input())
    cnt = 0
    for i in range(1,a+1):
        for j in range(1,1000000001):
            n = i*j
            if n[-1] == i:
                cnt+=1
    print(cnt)