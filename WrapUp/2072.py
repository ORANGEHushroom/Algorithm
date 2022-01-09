t = int(input())
for tc in range(1, t+1):
    num = list(map(int, input().split()))
    total = 0
    for i in num:
        if i % 2 :
            total += i

    print(f'#{tc} {total}')