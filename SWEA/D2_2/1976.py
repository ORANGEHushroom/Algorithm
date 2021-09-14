import sys
sys.stdin = open('1976.txt')

T = int(input())
for tc in range(1,T+1):
    print('#{}'.format(tc), end=" ")
    
    si1,bun1,si2,bun2 = map(int,input().split()) #시 1~12 분: 0~59
    if (bun1 + bun2)// 60 > 0: #60보다 크면
        new_si = si1 + si2 + (bun1 + bun2)//60 #몫을 더해주고
        new_bun = (bun1 + bun2) % 60
        if new_si > 12:
            new_si = new_si -12
    elif bun1 + bun2 <= 59:
        new_si = si1 + si2
        new_bun = bun1 + bun2
        if new_si > 12:
            new_si = new_si -12
    print(new_si,new_bun)