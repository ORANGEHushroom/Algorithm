T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size, w_len = map(int, input().split())
 
    mat = []
    
    for i in range(size):
        rows = list(input().split())
        mat.append(rows)
     
    test_ex= ''.join(['1']*w_len)
     
 
    cnt = 0
     
    #행에 대한 검사
    for row in mat:
        check=''.join(row).split('0')
        if test_ex in check:
            cnt += check.count(test_ex)
 
    #열에 대한 검사
    for x in range(size):
        check=[]
        for y in range(size):
            check.append(mat[y][x])
        check = ''.join(check).split('0')
        if  test_ex in check:
            cnt += check.count(test_ex)
     
    print('#{} {}'.format(test_case, cnt))


# import sys

# sys.stdin = open("input (2).txt")

# T = int(input())

# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     matrix = []
#     for _ in range(N):
#         matrix.append(list(map(int, input().split())))
#     total = 0
    
#     # 행우선
#     for col in range(N):
#         count = 0
#         for row in range(N):
#             if matrix[col][row] == 0:
#                 if count == K:
#                     total += 1
#                 count = 0
#             else:
#                 count += 1
#         if count == K:
#             total += 1
            
#     # 열우선
#     for row in range(N):
#         count = 0
#         for col in range(N):
#             if matrix[col][row] == 0:
#                 if count == K:
#                     total += 1
#                 count = 0
#             else:
#                 count += 1
#         if count == K:
#             total += 1

#     print("#{} {}".format(tc, total))   