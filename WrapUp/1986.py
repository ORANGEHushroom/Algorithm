t = int(input()) 
for tc in range(1, t+1):
    n = int(input())
    total = 0
    for i in range(1, n+1):
        if i % 2:
            total += i
        else:
            total -= i
    print(f'#{tc} {total}')