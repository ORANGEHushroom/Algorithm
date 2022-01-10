import sys
sys.stdin = open('input.txt')

t = int(input()) 
for tc in range(1, t+1):
    flag = 1
    li = [list(map(int,input().split())) for _ in range(9)]
    #가로
    for i in range(9):
        r1 = [0]*10
        for j in range(9):
            if r1[li[i][j]] == 0:
                r1[li[i][j]] = 1
        if sum(r1) != 9:
            flag = 0
        
    #세로
    newli = list(zip(*li))
    
    for i in range(9):
        r1 = [0]*10
        for j in range(9):
            if r1[newli[i][j]] == 0:
                r1[newli[i][j]] = 1
        if sum(r1) != 9:
            flag = 0
    #격자
    for x in range(3):
        for y in range(3):
            total = []
            for k in range(3):
                for h in range(3):
                    total.append(li[k][h])
            total.sort()
            if total != [1,2,3,4,5,6,7,8,9]:
                flag = 0

    print(f'#{tc} {flag}')
    