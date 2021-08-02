# T = int(input())
# for tc in range(1,T+1):
#     a = int(input())
#     total = []
#     for i in range(1,a**2+1):
#         total.append(i)
#         for j in range(1,a+1):
#             print(*total[:j*a+1], end="")
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    temp = N
    row = 0
    col = 0
    num = 1
    turn = 0
     
    while temp > 0 :
        if turn % 2 == 0:
            for i in range(col,temp):
                matrix[row][i] = num
                num += 1
                col = i
            if num == N**2:
                break
             
            row += 1
            for j in range(row,temp):
                matrix[j][col] = num
                num += 1
                row = j
            col -= 1
            turn += 1
            temp -= 1
        else:
            for i in range(col,N-2-temp,-1):
                matrix[row][i] = num
                num += 1
                col = i
            row -= 1
            for j in range(row,N-1-temp,-1):
                matrix[j][col] = num
                num += 1
                row = j
            col += 1
            turn += 1
    print(f'#{test_case}')
    for i in matrix:
        print(*i)