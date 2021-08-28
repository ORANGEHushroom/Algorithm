import sys
sys.stdin = open('input_ex.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = [list(map(str, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if li[i][j] == 'A':
                for a in range(-1,2):
                    if li[i+a][j] == 'H' and 0 <= i+a <= n-1:
                        li[i+a][j] = 'X'
                    if li[i][j+a] == 'H' and 0 <= j+a <= n-1:
                        li[i][j+a] = 'X'         

            elif li[i][j] == 'B':
                for b in range(-2,3):
                    if li[i+b][j] == 'H' and 0 <= i+b <= n-1:
                        li[i+b][j] = 'X'
                    if li[i][j+b] == 'H' and 0 <= j+b <= n-1:
                        li[i][j+b] = 'X'  
                
            elif li[i][j] == 'C':
                for c in range(-3,4):
                    if li[i+c][j] == 'H' and 0 <= i+c <= n-1:
                        li[i+c][j] = 'X'
                    if li[i][j+c] == 'H' and 0 <= j+c <= n-1:
                        li[i][j+c] = 'X'
    
    total = 0
    for k in range(n):
        total += li[k].count('H')
    print('#{} {}'.format(tc, total))



