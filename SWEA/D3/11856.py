import sys
sys.stdin = open('11856.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc),end=' ')
    a = []
    s = input()
    for i in s:
        if i not in a:
            a.append(i)
    
    flag = 0
    for j in a:
        if s.count(j) == 2:
            continue
        else:
            flag = 1
            
    if flag == 0:
        print('Yes')
    else:
        print('No')
    
