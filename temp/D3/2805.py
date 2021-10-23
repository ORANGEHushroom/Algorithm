import sys
sys.stdin = open('2805.txt')

t= int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input()) #7
    li = [list(map(int,input())) for _ in range(n)]
    h = n//2 #3
    i = 0
    a = 0
    total = 0
    while i <= h:
        total+=sum(li[i][h-a:h+a+1])
        a += 1
        i+=1
        if i > h:
            new_i = i
            new = total
            a = a
            break
    b = 1
    while i < n:
        new+=sum(li[i][b:n-b])
        b+=1
        i+=1
    print(new)