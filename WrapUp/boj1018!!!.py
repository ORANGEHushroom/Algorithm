## 뭔가가 안맞아서 못품 차후에 다시풀것

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

# 일단 아래는 예전 답안...
# N, M = map(int, input().split())
# board = list()
# for i in range(N):
#     board.append(input())
# repair = list()
# for i in range(N-7):
#     for j in range(M-7):
#         first_W = 0
#         first_B = 0
#         for k in range(i,i+8):
#             for l in range(j,j + 8):
#                 if (k + l) % 2 == 0: #(0,0) -> (0,2) (1,1) (3,3)
#                     if board[k][l] != 'W':#W가 아닐때
#                         first_W = first_W+1#W로 칠해주는 갯수
#                     if board[k][l] != 'B':
#                         first_B = first_B + 1
#                 else:
#                     if board[k][l] != 'B':
#                         first_W = first_W+1
#                     if board[k][l] != 'W':
#                         first_B = first_B + 1
#         repair.append(first_W)#체스판이 W로 시작할때 경우의 수
#         repair.append(first_B)#체스판이 B로 시작할때 경우의 수
# print(min(repair))