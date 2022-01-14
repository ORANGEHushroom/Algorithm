n , m = map(int, input().split())
li = [list(input()) for _ in range(n)]
result = []
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        
        if li[i][j] == "B":
            for a in range(i,i + 8):
                for b in range(j,j + 8):
                
                    #짝수홀수가 반복되면..00 01 02 03 04 05 
                    #더해서 홀수면
                    if (a+b) % 2 == 1:
                        if li[a][b] != "W":
                            cnt1 += 1
                    else:
                        if li[a][b] != "B":
                            cnt1 += 1
        else:
            for a in range(i,i + 8):
                for b in range(j,j + 8):
                    if (a+b) % 2 == 1:
                        if li[a][b] != "B":
                            cnt1 += 1 
                    else:
                        if li[a][b] != "W":
                            cnt1 += 1
        result.append(cnt1)
        
print(result)
print(min(result))
#아 왜안됨.. 아니면 걍 체스판 들고다니면서 비교를..