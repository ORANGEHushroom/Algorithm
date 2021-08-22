import sys
sys.stdin = open('input_num.txt')

T = int(input())
for tc in range(1, T+1):

    n = int(input())
    a = str(input())
    num = []
    for i in range(10):
        num.append([i,0])
    for i in a:
        num[int(i)][1] += 1
    max_val = 0
    max_li = []
    for i in range(10):
        if num[i][1] > max_val:
            max_val = num[i][1]
    for i in range(10):
        if num[i][1] == max_val:
            max_li.append(i)
    max_to = max_li[0]
    for i in max_li:
        if i > max_to:
            max_to = i
    print('#{} {} {}'.format(tc, max_to, num[max_to][1]))

        


            
        

    

    
