t = int(input()) 
for tc in range(1, t+1):
    li = list(map(int,input().split()))
    li.sort()
    print(f'#{tc} {round(sum(li[1:9])/8)}')