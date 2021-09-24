import sys
sys.stdin = open('11736.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = list(map(int,input().split()))
    total = 0 #5개라면
    for i in range(len(li)-2): # 1 2 3 -> 0 1 2 
        a = li[i:i+3]
        max_num = max(a)
        min_num = min(a)
        if a[1] != max_num and a[1] != min_num:
            total += 1
    print('#{} {}'.format(tc,total))

    # p[i]<p[i+1]<p[i+2] or p[i]>p[i+1]>p[i+2] 이렇게도가능!