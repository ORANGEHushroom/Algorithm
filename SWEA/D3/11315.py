import sys
sys.stdin = open('input.txt')

# skip
t = int(input())
for tc in range(1,t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())
    li = [list(map(str,input())) for _ in range(n)]
    # print(li) #[['.', '.', '.', '.', 'o'], ['.', '.', '.', 'o', '.'], ['.', '.', 'o', '.', '.'], ['.', 'o', '.', '.', '.'], ['o', '.', '.', '.', '.']]
    # 가로
    flag = 0
    for i in range(n):
        for j in range(n):
            #print(li[i][j:j+5])
            if li[i][j:j+5] == ['o', 'o', 'o', 'o', 'o'] and j+5<=n: #j-4 <= n-1
                flag = 1   

    # 세로
    for j in range(n): # 0 ~ n-1
        for i in range(n-5):
            # print(li[i:i+5][j])
            if li[i:i+5][j] == ['o', 'o', 'o', 'o', 'o'] and i+5<=n:
                flag = 1
                
            
    # 대각선
    vert_x = []
    for i in range(n):
        vert_x.append(li[i][i])
    for j in range(n):
        if vert_x[j:j+5] == ['o', 'o', 'o', 'o', 'o'] and j+5<=n:
            flag = 1

    vert_y = []
    for i in range(n):
        vert_y.append(li[n-i-1][n-i-1])
        for j in range(n):
            if vert_y[j:j+5] == ['o', 'o', 'o', 'o', 'o'] and j+5<=n:
                flag = 1
                

    if flag == 1:
        print('YES')
    else:
        print('NO')

    
