import sys
sys.stdin = open('input.txt')
### 나중에 다시 풀기!!
t = int(input()) 
for tc in range(1, t+1):
    n, length = map(int,input().split())
    li = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    result = 0
    
    for i in range(n):
        for j in range(n-1):
            if li[i][j] == 1 and li[i][j+1] == 1:
                cnt+=1
                if j+1 == n-1:
                    cnt+=1
                    if cnt != length:
                        cnt = 0
                    else:
                        result +=1
                        cnt = 0
            elif li[i][j] == 1 and li[i][j+1] == 0:
                cnt+=1
                if cnt != length:
                    cnt = 0
                else:
                    result +=1
                    cnt = 0
            elif li[i][j] == 0:
                cnt = 0
                continue
            elif j == n-1 and li[i][j] == 1:
                cnt+=1
                if cnt != length:
                    cnt = 0
                else:
                    result +=1
                    cnt = 0

    for i in range(n-1):
        for j in range(n):
            if li[j][i] == 1 and li[j][i+1] == 1:
                cnt+=1
                if i+1 == n-1:
                    cnt+=1
                    if cnt != length:
                        cnt = 0
                    else:
                        result +=1
                        cnt = 0
            elif li[j][i] == 1 and li[j][i+1] == 0:
                cnt+=1
                if cnt != length:
                    cnt = 0
                else:
                    result +=1
                    cnt = 0
            elif li[j][i] == 0:
                cnt = 0
                continue
            elif i == n-1 and li[j][i] == 1:
                cnt+=1
                if cnt != length:
                    cnt = 0
                else:
                    result +=1
                    cnt = 0


    print(f'#{tc} {result}')