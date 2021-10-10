import sys
sys.stdin = open('1216.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    li = [list(map(str,input())) for _ in range(100)]
    # 가로
    num = []
    for i in range(100):
        for j in range(100): #0~99
            for k in range(0,51):
                if li[i][j-k:j+1] == li[i][j:j+k+1] and j-k>=0 and j+k+1<=100: 
                    num.append(k)

    new_li = list(map(list, zip(*li)))
    for i in range(100):
        for j in range(100): #0~99
            for k in range(0,51):
                if li[i][j-k:j+1] == li[i][j:j+k+1] and j-k>=0 and j+k+1<=100: 
                    num.append(k)
    
    print(max(num))
                
            
