# x,y = map(int,input().split())

# for tc in range(1,y+1):
#     a = list(map(str,input().split()))
#     for i in range(1,x-6):
#         b = a[i:i+8]
#         count = 0
#         for j in range(len(b)):
#             if b[j] == b[j+1]:
#                 count+=1
#     print(count)
#     #x가 10일때 b는 2~10까지 슬라이싱 그러면 2:11 범위는 

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()
for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0: #(0,0) -> (0,2) (0,4) (2,0) (1,1) (3,3)
                    if board[k][l] != 'W':#W가 아닐때=> (0,0)이 b일때 +1 w라면 안칠해!
                        first_W = first_W+1#W로 칠해주는 갯수
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else: # (0,1) (0,3) (1,0)
                    if board[k][l] != 'B': #0,0dl W니까 옆인 너는 b라면 패스! 아니면 +1
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)#체스판이 W로 시작할때 경우의 수
        repair.append(first_B)#체스판이 B로 시작할때 경우의 수
print(min(repair))