import sys
sys.stdin = open('input.txt')
t = int(input()) 
for tc in range(1, t+1):
    n = int(input())
    li = [0]*10 #합 10
    cnt = 1
    while True:
        n = int(n)*cnt
        for i in str(n):
            if li[int(i)] == 0:
                li[int(i)] = 1
        if sum(li) == 10:
            n = int(n)//cnt
            break
        n = int(n)//cnt
        cnt += 1
    print(f'#{tc} {(cnt)*n}')