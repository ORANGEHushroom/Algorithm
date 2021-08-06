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
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)