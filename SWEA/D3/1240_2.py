import sys
sys.stdin = open('1240.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, m = map(int,input().split())
    li = [list(map(int,input())) for _ in range(n)]
    passw = []
    for i in range(n):
        for j in range(m-1,-1,-1):
            if li[i][j] != 0:
                passw.append(li[i][j-55:j+1])
                break
    a = passw[0]
    fin = []
    for i in range(0,len(a)-1,7):
        if a[i:i+7] == [0,0,0,1,1,0,1]:
            fin.append('0')
        elif a[i:i+7] == [0,0,1,1,0,0,1]:
            fin.append('1')
        elif a[i:i+7] == [0,0,1,0,0,1,1]:
            fin.append('2')
        elif a[i:i+7] == [0,1,1,1,1,0,1]:
            fin.append('3')
        elif a[i:i+7] == [0,1,0,0,0,1,1]:
            fin.append('4')
        elif a[i:i+7] == [0,1,1,0,0,0,1]:
            fin.append('5')
        elif a[i:i+7] == [0,1,0,1,1,1,1]:
            fin.append('6')
        elif a[i:i+7] == [0,1,1,1,0,1,1]:
            fin.append('7')
        elif a[i:i+7] == [0,1,1,0,1,1,1]:
            fin.append('8')
        elif a[i:i+7] == [0,0,0,1,0,1,1]:
            fin.append('9')
    
    ans = 0
    for i in range(8):
        if i%2:
            ans+= int(fin[i])
        else:
            ans+=int(fin[i])*3
    b = 0
    if ans%10 == 0:
        for i in range(8):
            b+= int(fin[i])
        print(b)
    else:
        print(0)